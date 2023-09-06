from django.http import HttpResponse, HttpResponseNotFound
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

def logout(request) :
    del request.session['auth']
    del request.session['password']
    del request.session['mail']
    del request.session['profile']
    return render(request,'log.html',{
        "massage":"การออกจากระบบเสร็จสิ้น"
    })

def add_media(media) :
    fs=FileSystemStorage()
    x = datetime.datetime.now()
    f_type = media.name.split(".")
    f_type = f_type[1]
    f_name = x.strftime("%d") + '-' + x.strftime("%m")  + '-' + x.strftime("%Y") + '-' + str(random.randrange(100000, 999999)) + '.' + f_type
    filename = fs.save(f_name, media)
    return fs.url(filename)

def id() :
    x = datetime.datetime.now()
    return x.strftime("%d") + x.strftime("%m") + x.strftime("%Y") + str(random.randrange(100000, 999999))
def date() :
    x = datetime.datetime.now()
    return x.strftime("%d") + '/' + x.strftime("%m") + '/' + x.strftime("%Y")

    


    
