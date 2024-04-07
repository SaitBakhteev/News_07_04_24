from django import forms
from .models import Post, Author
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    title=forms.CharField(label='Название', max_length=200)
    author = forms.ModelChoiceField(queryset=Author.objects.all(),label='автор поста')
    content=forms.CharField(widget=forms.Textarea, label='Текст статьи')


    class Meta:
        model = Post
        fields=[]


    # def clean(self):
    #     clean_post = super().clean()
    #     title = clean_post.get('title')
    #     if len(title)<25:
    #         raise ValidationError({'title':'Нельзя писать плохиев слова'})
    #     return clean_post
