from django import forms
from . import models


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        title = self.cleaned_data.get("title")
        text = self.cleaned_data.get("text")
        if not title or not text:
            raise forms.ValidationError('Заполните все поля')

    def save(self):
        title = self.cleaned_data.get("title")
        text = self.cleaned_data.get("text")
        question = models.Question(title=title, text=text)
        question.save()
        return question


class AnswerForm(forms.Form):
    question = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        question = self.cleaned_data.get("question")
        text = self.cleaned_data.get("text")
        if not question or not text:
            raise forms.ValidationError('Заполните все поля')

    def save(self):
        question = self.cleaned_data.get("question")
        text = self.cleaned_data.get("text")
        answer = models.Answer(text=text, question_id=question)
        answer.save()
        return answer
