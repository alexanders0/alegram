""" User forms """

# Django
from django import forms


class ProfileForm(forms.Form):
    website = forms.URLField(label='Website', max_length=200, required=True)
    biography = forms.CharField(
        label='Biography',
        max_length=500,
        required=False)
    phone_number = forms.CharField(
        label='Phone number',
        max_length=20,
        required=False)
    picture = forms.ImageField()
