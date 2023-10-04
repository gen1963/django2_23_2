from django import forms
from .models import Post, Comments_post, Photo


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published', "user")

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments_post
        fields = ('user_name', 'email', 'description', 'date_comments')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('__all__')