from django.contrib import admin

from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Register your models here.
admin.site.register(Contact)
