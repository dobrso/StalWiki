from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description']

    def clean_description(self):
        description = self.cleaned_data['description']
        if description:
            description = description.strip()
            description = f'{description[0].upper()}{description[1:]}.'
        return description
