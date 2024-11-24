from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import TextInput, Textarea, ModelForm

# Create your models here.
class Settings(models.Model):

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=255)
    smtp_server = models.CharField(blank=True, max_length=100)
    smtp_email = models.CharField(blank=True, max_length=100)
    smtp_password = models.CharField(blank=True, max_length=100)
    smtp_port = models.CharField(blank=True, max_length=5)
    youtue = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    facebook = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True, upload_to='images/')
    aboutus = RichTextUploadingField(null=False)
    contact = RichTextUploadingField(null=False)

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    STATUS = (('New', 'New'),
              ('Read', 'Read'),
              ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'subject', 'message']
        widjets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'})
        }