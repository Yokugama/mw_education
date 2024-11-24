"""
URL configuration for my_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as w
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('selectlanguage/', w.selectlanguage, name='selectlanguage'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns (
    path(_('admin/'), admin.site.urls),
    path('home', include('home.urls')),
    path('', w.index, name='home'),
    path('course/', include('course.urls')),
    path('course/', w.courses, name='courses'),
    path('about/', w.about, name='about'),
    path('contact/', w.contact, name='contact'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('tutor/', w.tutors, name='tutors'),
    path('student/', w.students, name='students'),
    path('subject/<int:id>/<slug:slug>/', w.subject_detail, name='subject_detail'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)