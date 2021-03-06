from django.db import models
from django.urls import reverse
# Create your models here.

class User(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question (models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})


class Answer (models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

class Session(models.Model):
    key = models.CharField(unique=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    expires = models.DateTimeField()