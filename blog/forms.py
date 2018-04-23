from django import forms
from .models import Post, Like

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag')
        
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag')
        
class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ()