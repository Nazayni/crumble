from django import forms
from .models import Note # Make sure to import your Post model

class NoteUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["banner"].required = False
        self.fields["banner"].widget.attrs.update({
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
            'placeholder': 'Note Title',
            'maxlength': '100',
            'minlength': '5'
        })
        self.fields["slug"].widget.attrs.update({
            'required': '',
            'name': 'slug',
            'id': 'slug',
            'type': 'text',
            'class': 'form-input',
            'placeholder': 'Note Slug',
            'maxlength': '100',
            'minlength': '5'
        })
        self.fields["body"].widget.attrs.update({
            'required': '',
            'name': 'body',
            'id': 'body',
            'class': 'form-input',
            'placeholder': 'Note Body',
            'rows': '5',
            'cols': '50'
        })

    class Meta:
        model = Note
        fields = ['banner', 'title', 'slug', 'body']
