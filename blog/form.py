from django import forms
from blog.models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
