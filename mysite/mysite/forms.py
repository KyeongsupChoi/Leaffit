# -*- encoding: utf-8 -*-


from django import forms
from .models import RepMax


class WendlerForm(forms.ModelForm):
    """Form for the image modelsss"""
    class Meta:
        model = RepMax
        fields = ('weight',)

    weight = forms.IntegerField()

