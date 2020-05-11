from django.shortcuts import render
from blog.models import Post, Category, Legales, Sobremi

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{
        'posts' : posts
    })

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {
        'posts' : posts
    })

def categorias(request):
    categorias = Category.objects.all()
    return render(request, 'categorias.html', {
        'categorias' : categorias,
    })

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {
        'post': post
    })

def categoria(request,id):
    category = Category.objects.get(id=id)
    post = Post.objects.filter(category=category)
    return render(request, 'categoria.html',{
        'category' : category,
        'post' : post
    })

def sobremi(request):
    sobremi = Sobremi.objects.all()
    return render(request, 'sobremi.html',{
        'sobremi' : sobremi
    })

def privacidad(request, id):
    privacidad = Legales.objects.get(id=id)
    return render(request, 'privacidad.html', {
        'privacidad' : privacidad
    })

def politicas(request, id):
    politicas = Legales.objects.get(id=id)
    return render(request, 'politicas.html',{
        'politicas' : politicas
    })


