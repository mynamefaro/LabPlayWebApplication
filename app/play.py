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


def index(request,id) :
    if request.session.get('auth') :
        games = database.search(u'games',u'id',id)
        data = {
            "games" : games[0],
        }
        return render(request,'gameview.html',data)
    else :
        return redirect('/login/')
    
def dashboard(request,id) :
    if request.session.get('auth') :
        if request.is_ajax() :
            di = request.GET.get('id')
            player = database.search(u'players',u'dash_id',di)
            return JsonResponse(player ,safe=False)
        else :
            pin = str(random.randrange(100000, 999999))
            di = methods.id()
            data = {
                u'pin' : pin,
                u'creator' : request.session.get('auth'),
                u'date' : methods.date() ,
                u'id' : di,
                u'name' : ""
            }
            database.add(u'playing_records',di,data)
            return render(request,'dashboard.html',{
                'PIN' : pin,
                'id' : di
            })
    else:
        return redirect('/login/')
def like(request,id) :
    doc = database.get_doc(u'games',id)
    like = doc.get('like')
    like = like + 1
    print("It's like")
    print(like)
    database.update(u'games',id,{u'like':int(like)})
    return JsonResponse(doc)

def mobile(request) :
    return render(request,'mobile.html')

def finish(request,id) :
    if request.method == "POST" : 
        name = request.POST.get('name')
        database.update(u'playing_records',id,{
            u'name' : name,
            u'pin' : "-"
        })
    else :
        doc = database.get_doc(u'playing_records',id)
        pin = doc.get('pin')
        database.search_delete(u'playing_records',u'id',id)
    return redirect('/index/')

