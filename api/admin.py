from api.models import Publication
from django.contrib import admin

from .models import Student, Book, Copyright, Publication, Author

admin.site.register([Student, Book, Copyright, Publication, Author])
