from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.utils import translation
from django.conf import settings
from home.models import Settings, ContactForm, ContactMessage
from course.models import Course
from course.models import Subject
from course.models import Tutor
from course.models import Student
import requests
# Create your views here.
def index(request):
    setting = Settings.objects.get()
    course = Course.objects.all()
    sebject_cr = Subject.objects.all().order_by('id')[:3]
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    student_cr = Student.objects.all().order_by('id')[:3]
    page = 'home'

    context = {
        'setting': setting,
        'page': page,
        'sebject_cr': sebject_cr,
        'tutor_cr': tutor_cr,
        'student_cr': student_cr,
        'course': course
    }
    return render(request, 'index.html', context)

def about(request):
    setting = Settings.objects.get()
    context = {
        'setting': setting
    }
    return render(request, 'about.html', context)


TELEGRAM_BOT_TOKEN = '7851922547:AAGySHzjYPWnvmJAEOv49cY-WMOwp1X4JH4'
TELEGRAM_CHANNEL = '@zayavka_uz'

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            ip = request.META.get('REMOTE_ADDR')
            message_text = f'New message:\n\nName: {name} \nPhone: {phone} \nIP: {ip} \nSubject: {subject} \nMessage: {message}'
            telegram_api_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
            telegram_params = {'chat_id': {TELEGRAM_CHANNEL}, 'text': message_text}
            requests.post(telegram_api_url, params = telegram_params)

            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip= request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Thanks, "+ data.name + ". We received your message and will respond shortly...")
            return HttpResponseRedirect('/contact')

    setting = Settings.objects.get()
    context = {
        'setting': setting
    }
    return render(request, 'contact.html', context)

def tutors(request):
    setting = Settings.objects.get()
    tutor_cr = Tutor.objects.all().order_by('id')
    context = {
        'tutor_cr': tutor_cr,
        'setting': setting
    }
    return render(request, 'tutors.html', context)

def students(request):
    setting = Settings.objects.get()
    student_cr = Student.objects.all().order_by('id')
    context = {
        'student_cr': student_cr,
        'setting': setting
    }
    return render(request, 'students.html', context)


def courses(request):
    setting = Settings.objects.get()
    course_cr = Subject.objects.all().order_by('id')
    context = {
        'course_cr': course_cr,
        'setting': setting
    }
    return render(request, 'courses.html', context)


def subject_detail(request, id, slug):
    # id va slug bo'yicha subjectni topish
    subject = get_object_or_404(Subject, id=id, slug=slug)

    # Boshqa subjectlarni olish (so'nggi 4 ta)
    subject_cr = Subject.objects.all().order_by('id')[:4]
    # Ushbu subjectga tegishli ustozlarni olish
    tutor_cr = Tutor.objects.filter(subject=subject).order_by('id')[:4]
    
    # Kontekstni yaratish
    context = {
        'subject_cr': subject_cr,
        'subject': subject,
        'tutor_cr': tutor_cr
    }

    # Template'ga yuborish
    return render(request, 'subject_detail.html', context)


def selectlanguage(request):
    if request.method == 'POST':

        lang  = request.POST['language']
        translation.activate(lang)
        request.session[settings.LANGUAGE_COOKIE_NAME] = lang
        return HttpResponseRedirect('/' + lang)