from api.models import Publication
from django.contrib import admin

from api.models.ContainerStatus import ContainerStatus


from .models import Student, Book, Copyright, Publication, Author

from api.models.Agent import Agent
from api.models.App import App

admin.site.register([Student, Book, Copyright, Publication, Author, App, Agent, ContainerStatus])
