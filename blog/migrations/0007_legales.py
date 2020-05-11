# Generated by Django 3.0.6 on 2020-05-10 15:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200509_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', ckeditor.fields.RichTextField()),
                ('fecha_actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]