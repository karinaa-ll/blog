from django import forms
from .models import Post, Category, Tag, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content'] 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'status', 'categories', 'tags', 'image']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'content': forms.Textarea(attrs={'placeholder': 'Ваш пост', 'rows': 4}),
        }  

    # Это дополнительные поля для выбора категорий и тегов
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)