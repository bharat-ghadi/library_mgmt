from django.contrib import admin
from .models import Genre, BookData, Membership, UserData, BookStatus, Workspace

# Register your models here.

admin.site.register(Genre)
admin.site.register(BookData)
admin.site.register(UserData)
admin.site.register(Membership)
admin.site.register(BookStatus)
admin.site.register(Workspace)
