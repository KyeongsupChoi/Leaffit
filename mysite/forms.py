# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from .models import RepMax


class WendlerForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = RepMax
        fields = ('weight',)

    weight = forms.IntegerField()

