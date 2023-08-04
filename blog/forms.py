from django import forms
from .models import Post, Comment


# form for adding posts
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


# form for adding posts
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)