from django import forms

from .models import *


class ReviewForm(forms.ModelForm):
    """ Review Form """

    class Meta:
        model = Review
        fields = ("name", "email", "text")
