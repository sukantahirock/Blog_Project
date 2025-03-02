from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # ফর্মে টাইটেল ও কনটেন্ট থাকবে
