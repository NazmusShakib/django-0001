from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from register.models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 error_messages={'required': 'Please let us know what to call you!'})
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.',
                                error_messages={'required': 'Please let us know what to call you!'})
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))
    location = forms.CharField(max_length=100, required=True, help_text='Required optional.')
    birth_date = forms.CharField(max_length=100, required=True, help_text='Required optional.')

    class Meta:
        model = Profile
        fields = [
            'bio',
            'location',
            'birth_date',
        ]
