from django.contrib import admin

from api.models import Publication
from api.models.Agent import Agent
from api.models.App import App
from api.models.Camera import Camera
from api.models.ContainerStatus import ContainerStatus

from .models import Author, Book, Copyright, Publication, Student

admin.site.register([Student, Book, Camera, Copyright, Publication, Author, App, Agent, ContainerStatus])
