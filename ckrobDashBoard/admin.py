from django.contrib import admin

# Register your models here.
from ckrob.ckrobDashBoard.models import Author

class AuthorAdmin(admin.Model.Admin):
    pass
admin.site.register(Author, AuthorAdmin)
