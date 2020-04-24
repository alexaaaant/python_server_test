from django import forms
from . import models


class AnswerForm(forms.Form):
    question = forms.CharField(max_length=100)
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
