from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        self.cleaned_data['author_id'] = 1
        question = Question(**self.cleaned_data)
        #question.author_id = self._user.id
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def save(self):
        self.cleaned_data['author_id'] = 1
        answer = Answer(**self.cleaned_data)
        #answer.author_id = self._user.id
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError(
                u'Username is empty', code='validation_error')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.strip() == '':
            raise forms.ValidationError(
                u'Email is empty', code='validation_error')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError(
                u'Password is empty', code='validation_error')
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError(
                u'Username is empty', code='validation_error')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError(
                u'Password is empty', code='validation_error')
        return password

    def save(self):
        user = authenticate(**self.cleaned_data)
        return user
