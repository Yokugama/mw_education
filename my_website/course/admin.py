from django.contrib import admin

# Register your models here.
from course.models import Course
from course.models import Subject
from course.models import Student
from course.models import Tutor

class CouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image_tag']
    readonly_fields = ('image_tag',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'image_tag']
    list_filter = ['course']
    readonly_fields = ('image_tag',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image_tag']
    readonly_fields = ('image_tag',)

class TutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'image_tag']
    list_filter = ['subject']
    readonly_fields = ('image_tag',)

admin.site.register(Course, CouseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)