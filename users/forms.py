from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':     '',
            'name':         'username',
            'id':           'username',
            'type':         'text',
            'class':        'form-input',
            'placeholder':  'John Doe',
            'maxlength':    '16',
            'minlength':    '6',
        })
        self.fields["email"].widget.attrs.update({
            'required':     '',
            'name':         'email',
            'id':           'email',
            'type':         'email',
            'class':        'form-input',
            'placeholder':  'johndoe@gmail.com',
        })
        self.fields["password1"].widget.attrs.update({
            'required':     '',
            'name':         'password1',
            'id':           'password1',
            'type':         'password',
            'class':        'form-input',
            'placeholder':  'password',
            'maxlength':    '22',
            'minlength':    '8',
        })
        self.fields["password2"].widget.attrs.update({
            'required':     '',
            'name':         'password2',
            'id':           'password2',
            'type':         'password',
            'class':        'form-input',
            'placeholder':  're-type password',
            'maxlength':    '22',
            'minlength':    '8'
        })

    def save(self, commit=True):
        user = super().save(commit)
        Profile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    def __init__(self, request = None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':     '',
            'name':         'username',
            'id':           'username',
            'type':         'text',
            'class':        'form-input',
            'placeholder':  'John Doe',
            'maxlength':    '16',
            'minlength':    '6',
        })
        self.fields["password"].widget.attrs.update({
            'required':     '',
            'name':         'password',
            'id':           'password',
            'type':         'password',
            'class':        'form-input',
            'placeholder':  'Enter Password',
        })

    class Meta: 
        model = User
        fields = ['username', 'password']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'links']