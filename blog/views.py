import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import CreateView

from .forms import PostForm, CommentsForm
from .models import Post, Category
# from .utils import *

def gummy():
    return str(random.randint(10, 200))

def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count // 2 + 1
    return {"cat1": all[:half], "cat2": all[half:]}

def index(request):
    # posts = Post.objects.all()
    # posts = Post.objects.filter(title__contains = 'python')
    # posts = Post.objects.filter(published__year=2023)
    # posts = Post.objects.filter(category__name__iexact='it')
    posts = Post.objects.order_by('-published')
    # post = Post.objects.get(pk=2)
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)

def post(request, title=None):
    post = get_object_or_404(Post, title=title)
    context = {"post": post}
    context.update(get_categories())
    return render(request, "blog/post.html", context=context)

def category(request, id=None):
    c = get_object_or_404(Category, pk=id)
    posts = Post.objects.filter(category=c).order_by('-published')
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)

def about(request):
    return render(request, "blog/about.html")

def services(request):
    return render(request, "blog/services.html")

def contacts(request):
    return render(request, "blog/contacts.html")

def pro_url(request, dynamic_url):
    print(dynamic_url)
    return render(request, "blog/services.html", context={"url": dynamic_url})

def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context=context)

@login_required
def create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published = now()
            post.user = request.user
            post.save()
            return index(request)
    context = {'form': form}
    return render(request, "blog/create.html", context=context)

# def comments_post(request):
#     post = Post.objects.get(id=pk)
#     context = {"post": post}
#     return render(request, 'blog/post.html', context=context)

def post_com(request, pk):
    # comments = Comments.objects.filter(post=post)
    # form = CommentsForm()
    form = CommentsForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.post_id = pk
        form.save()
    # return redirect(f'blog/{pk}')
    return render(request, 'blog/index.html')

@login_required
def profile(request):
    context = {"user": request.user}
    return render(request, 'blog/profile.html', context=context)

@login_required
def register(request):
    context = {"user": request.user}
    return render(request, 'blog/register.html', context=context)

# class RegistereUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'blog/register.html'
#     success_url = reverse_lazy('login')

