from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


from . forms import *
from . models import *


# Create your views here.

# Menu references

def home_page(request):
    return render(request, 'index.html', {})


def contact_page(request):
    return render(request, 'contact.html', {})


def about_page(request):
    return render(request, 'about.html', {})


def portfolio_page(request):
    return render(request, 'portfolio.html', {})





# Contact form

def get_in_touch(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            to_email = ['seitakhunova@gmail.com']
            send_mail(subject, message, email, to_email, fail_silently=False)
    return redirect('home')


# Blog

def blog_page(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'page': page, 'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})