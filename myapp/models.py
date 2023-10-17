from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Topic(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(User, through='Preference')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        article = self.article_set.first()
        if article:
            return article.get_absolute_url()

        return reverse('myapp:list_topics')


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myapp:show_article',
                       args=[str(self.pk)])


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, models.DO_NOTHING)

    def __str__(self):
        return self.message


class Preference(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_notified = models.BooleanField(default=False)
