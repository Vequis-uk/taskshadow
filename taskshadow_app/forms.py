from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from taskshadow_app.models import TaskShadowTodo


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Enter Your Username'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Enter Your Password'})
    )

# User Creation


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Confirm Your Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Enter Your Username'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Enter Your Email'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

# New form for updating the to-do titles
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskShadowTodo
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'edit-title-input'})
        }