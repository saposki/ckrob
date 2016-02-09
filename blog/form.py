from django import forms
from blog.models import Upload

class UploadForm(forms.ModelForm):
    dataSet = forms.FileField(label='Select a .csv file')
