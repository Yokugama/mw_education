# Generated by Django 5.1.2 on 2024-11-09 13:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_description_alter_course_keywords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
