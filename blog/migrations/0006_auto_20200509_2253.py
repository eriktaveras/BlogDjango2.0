# Generated by Django 3.0.6 on 2020-05-10 02:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200509_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
