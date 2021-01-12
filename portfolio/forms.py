from django import forms
from .models import Comment


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    to_email = ['seitakhunova@gmail.com']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')