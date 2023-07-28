from django import forms

from django import forms
# from django.db import models
from django.core.validators import MaxLengthValidator


class UploadFileForm(forms.Form):
    # input = models.TextField(max_length=250, blank=True,validators=[MaxLengthValidator(250)])
    # input = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name'}),label=(u'First name'),required=False)
    details = forms.CharField(widget=forms.Textarea)


# message =forms.widgets.TextInput()
'''
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )'''


class it_sales_form(forms.Form):
    '''
    var = forms.CharField(max_length=50)
    '''