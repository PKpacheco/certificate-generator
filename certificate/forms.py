# coding:utf-8
from django import forms
from .models import Certificate


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('name', 'text_1', 'text_2', 'date', 'text_3', 'time', 'logo')
