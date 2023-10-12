from django.http import HttpResponse, HttpRequest
from django.http import Http404
from django.shortcuts import render
from datetime import datetime


def show_about(request):
    return render(request, template_name='about.html')


def show_home_page(request):
    return render(request, template_name='base.html')


def show_article(request, article_id):
    return render(request, template_name='articles.html')


def add_comment(request, article_id) -> HttpResponse:
    return HttpResponse("Add comment here")


def create_article(request):
    return render(request, template_name='create_article.html')


def update_article(request, article_id) -> HttpResponse:
    return HttpResponse("Article update")


def delete_article(request, article_id) -> HttpResponse:
    return HttpResponse("Article delete")


def list_topics(request):
    return render(request, template_name='topics.html')


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
    return render(request, template_name='register.html')


def user_login(request):
    return render(request, template_name='login.html')


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

