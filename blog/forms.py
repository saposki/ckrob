from django import forms
# from blog.models import Upload

class UploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    dataSet = forms.FileField(label='Select a *.csv file')
