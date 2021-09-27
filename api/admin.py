from django.contrib import admin

from .models import Student, Book, Copyright

admin.site.register([Student, Book, Copyright])
