from django import forms

from .models import Guide


class GuideCreateForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ['name', 'description', 'tags']