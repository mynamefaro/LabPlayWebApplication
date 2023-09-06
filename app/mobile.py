from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from django.shortcuts import render,redirect
from django.template import loader
from . import database
from . import methods
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files import File
import random
import datetime

#-----INDEX------






