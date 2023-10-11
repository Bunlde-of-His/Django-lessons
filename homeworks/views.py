from django.shortcuts import render


def show_base(request):
    return render(request, template_name='base.html')


def show_articles(request):
    return render(request, template_name='articles.html')


def show_full_articles(request):
    return render(request, template_name='full_articles.html')


def show_about(request):
    return render(request, template_name='about.html')


def show_topics(request):
    return render(request, template_name='topics.html')


def show_register(request):
    return render(request, template_name='register.html')


def show_login(request):
    return render(request, template_name='login.html')


def show_create_article(request):
    return render(request, template_name='create_article.html')