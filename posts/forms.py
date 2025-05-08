from django import forms
from .models import Post # Make sure to import your Post model

class PostUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["banner"].widget.attrs.update({
            'required': '',
            'name': 'banner',
            'id': 'banner',
            'class': 'form-input',
            'placeholder': 'Select banner image'
        })
        self.fields["title"].widget.attrs.update({
            'required': '',
            'name': 'title',
            'id': 'title',
            'type': 'text',
            'class': 'form-input',
            'placeholder': 'Post Title',
            'maxlength': '100',
            'minlength': '5'
        })
        self.fields["slug"].widget.attrs.update({
            'required': '',
            'name': 'slug',
            'id': 'slug',
            'type': 'text',
            'class': 'form-input',
            'placeholder': 'Post Slug',
            'maxlength': '100',
            'minlength': '5'
        })
        self.fields["body"].widget.attrs.update({
            'required': '',
            'name': 'body',
            'id': 'body',
            'class': 'form-input',
            'placeholder': 'Post Body',
            'rows': '5',
            'cols': '50'
        })

    class Meta:
        model = Post
        fields = ['banner', 'title', 'slug', 'body']
