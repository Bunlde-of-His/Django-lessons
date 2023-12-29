from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, reverse
from datetime import datetime
from myapp.models import Article, Topic, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import AuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login
from .forms import ArticleForm
from .forms import CommentForm


def show_about(request):
    return render(request, template_name='myapp/about.html')


def show_home_page(request):
    topics = Topic.objects.all()
    articles = Article.objects.all()
    return render(request, template_name='myapp/articles.html', context={'topics': topics, 'articles': articles})


def filtered_articles(request, topic_id):
    selected_topic = Topic.objects.get(pk=topic_id)
    articles = Article.objects.filter(topics=selected_topic)
    topics = Topic.objects.all()
    return render(request, 'myapp/articles.html', {'articles': articles, 'topics': topics})


def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            return redirect('myapp:show_article', article_id=article_id)
    else:
        comment_form = CommentForm()

    return render(request, 'myapp/detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form
    })


def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('myapp:show_article', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'myapp/detail.html', {'form': form, 'article': article})


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            topic_ids = request.POST.getlist('topics')
            article.topics.set(topic_ids)

            return redirect('myapp:articles')
    else:
        form = ArticleForm()

    return render(request, 'myapp/create_article.html', {'form': form})


def update_article(request, article_id) -> HttpResponse:
    return HttpResponse("Article update")


def delete_article(request, article_id) -> HttpResponse:
    return HttpResponse("Article delete")


def subscribe_to_topic(request, topic) -> HttpResponse:
    return HttpResponse("Subscribe to topic")


def unsubscribe_from_topic(request, topic) -> HttpResponse:
    return HttpResponse("Unsubscribe from topic")


def user_profile(request, username) -> HttpResponse:
    return HttpResponse("User profile")


def set_password(request) -> HttpResponse:
    return HttpResponse("Set password")


def set_userdata(request) -> HttpResponse:
    return HttpResponse("Set userdata")


def deactivate_account(request) -> HttpResponse:
    return HttpResponse("Account deactivate")


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')


    else:
        form = AuthenticationForm()

    return render(request, 'myapp/login.html', {'form': form})


def user_logout(request) -> HttpResponse:
    return HttpResponse("User logout")


def show_date(request, year, month):
    try:
        year = int(year)
        month = int(month)

        if not (1 <= month <= 12):
            raise ValueError("Invalid month")

        if year < 2000:
            raise Http404("No data")

        current_date = datetime.now().date()
        date = datetime(year, month, 1).date()

        if date >= current_date:
            raise Http404("Date has not occurred yet")
    except ValueError:
        raise Http404("Invalid date format")

    return HttpResponse(f"Date: {date}")
