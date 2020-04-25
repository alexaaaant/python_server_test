from django import forms
from . import models
from datetime import datetime

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        title = self.cleaned_data.get("title")
        text = self.cleaned_data.get("text")
        if not title or not text:
            raise forms.ValidationError('acds')

    def save(self):
        title = self.cleaned_data.get("title")
        text = self.cleaned_data.get("text")
        question = models.Question(title=title, text=text, author=self._user)
        question.save()
        return question


class AnswerForm(forms.Form):
    question = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        question = self.cleaned_data.get("question")
        text = self.cleaned_data.get("text")
        if not question or not text:
            raise forms.ValidationError('acds')

    def save(self):
        question = self.cleaned_data.get("question")
        text = self.cleaned_data.get("text")
        answer = models.Answer(text=text, question_id=question, author=self._user)
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField()

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        email = self.cleaned_data.get("email")
        if not username or not password or not email:
            raise forms.ValidationError('acds')
        user = models.User.objects.filter(username=username)
        if user:
            raise forms.ValidationError('acds')

    def save(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        email = self.cleaned_data.get("email")
        user = models.User(username=username, password=password, email=email)
        user.save()
        return user
