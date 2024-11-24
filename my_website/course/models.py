from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = RichTextUploadingField(null=False)
    image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(null=False, unique=True)
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50" />' .format(self.image.url))
    
    image_tag.short_description = 'Image'
    

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    subject_tutor = models.CharField(max_length=100)
    description = RichTextUploadingField(null=False)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.CharField(max_length=10)
    detail = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50" />' .format(self.image.url))
    
    image_tag.short_description = 'Image'
    

class Student(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField(null=False, blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    
    def __str__(self):
        return self.name
    
    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50" />' .format(self.image.url))
    
    image_tag.short_description = 'Image'
    

class Tutor(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = RichTextUploadingField(null=False)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name
    
    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50" />' .format(self.image.url))
    
    image_tag.short_description = 'Image'