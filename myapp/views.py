from django.http import HttpResponse, HttpRequest
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from myapp.models import Article, Comment, Topic


def show_about(request):
    return render(request, template_name='myapp/about.html')


def show_home_page(request):
    articles = Article.objects.all()
    return render(request, template_name='myapp/articles.html', context={'articles': articles})


def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id,)
    comments = Comment.objects.filter(article=article_id)
    return render(request, template_name='myapp/detail.html', context={'article': article, 'comments': comments})


def add_comment(request, article_id) -> HttpResponse:
    return HttpResponse("Add comment here")


def create_article(request):
    return render(request, template_name='myapp/create_article.html')


def update_article(request, article_id) -> HttpResponse:
    return HttpResponse("Article update")


def delete_article(request, article_id) -> HttpResponse:
    return HttpResponse("Article delete")


def list_topics(request):
    topics = Topic.objects.all()
    return render(request, template_name='myapp/topics.html',  context={'topics': topics})


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
    return render(request, template_name='myapp/register.html')


def user_login(request):
    return render(request, template_name='myapp/login.html')


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
