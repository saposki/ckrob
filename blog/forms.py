# from django import forms
# # from .models import Post
#
# from .models import UploadFile
#
# # class UploadForm(forms.Form):
# #     title = forms.CharField(max_length=50)
# #     file = forms.FileField(label='*.csv file')
#
# class UploadForm (forms.Form):
#     class Metta:
#         model = UploadFile
#         fields = [
#             'title',
#             'file',
#
#         ]


from django import forms

from .models import UploadFile

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = [
            'title',
            'file'
        ]
