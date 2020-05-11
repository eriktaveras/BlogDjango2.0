from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()
    content = RichTextField()
    fecha = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="imagen", default="imagen/default.jpg")

    def __str__(self):
        return self.title

class Legales(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    fecha_actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Sobremi(models.Model):
    saludo = models.CharField(max_length=150)
    content = RichTextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.saludo



    