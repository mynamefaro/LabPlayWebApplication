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

def default(request) :
    return render(request,'default.html')
    
def index(request) :
    if request.is_ajax() :
        di = request.GET.get('id')
        games = database.search(u'games',u'id',di)
        return JsonResponse(games[0])
    else :
        games = database.get(u'games')
        data = {
            "games" : games
        }
        return render(request,'index.html',data)

def contact(request) :
    return render(request,'contact.html')

#-----SEARCH-----

def search(request) :
    if request.method == "GET" :
        search = request.GET.get('search')
        games = []
        name_type = database.search(u'games',u'name',search) #NAME FIND
        for game in name_type :
            games.append(game)
        sub_type = database.search(u'games',u'type',search) #SUBJECT FIND
        for game in sub_type :
            games.append(game)
        create_type = database.search(u'games',u'creator',search) # CREATOR FIND
        for game in create_type :
            games.append(game)
        data = {
            "games" : games,
        }
        if games == [] :
            data.update({"massage":"ไม่พบข้อมูลที่ท่านต้องการ"})
        return render(request,'search.html',data)
#-----LOGIN------


def login(request) :
    if request.method == "POST" :
        username = request.POST.get('user')
        password = request.POST.get('pass')
        auth_user = database.get_doc(u'users',username)
        if auth_user == "error" :
            return render(request,'login.html',{
                    "massage":"ไม่พบผู้ใช้งาน"
            })
        if not(auth_user == {}) :
            if auth_user.get("password") == password :
                request.session['auth'] = auth_user.get('username')
                request.session['profile'] = auth_user.get('profile')
                request.session['password'] = auth_user.get('password')
                request.session['mail'] = auth_user.get('e-mail')
                return render(request,'log.html',{
                    "massage":"เข้าสู่ระบบสำเร็จ"
                })
            else :
                return render(request,'login.html',{
                    "massage":"รหัสผ่านไม่ถูกต้อง"
                })
        else :
            return render(request,'login.html',{
                    "massage":"ไม่พบผู้ใช้งาน"
            })
    else :
        return render(request,'login.html')


#-----REGIS------


def regis(request) :
        if request.method == "POST" :
            name = request.POST.get('name')
            mail = request.POST.get('mail')
            password = request.POST.get('pas')
            bd = request.POST.get('bd')
            genre = request.POST.get('gen')
            job = request.POST.get('job')
            profile = request.FILES.get('profile')
            if profile != '':
                uploaded_file_url = methods.add_media(profile)
            data = {
                u'username' : name,
                u'id' : methods.id(),
                u'e-mail' : mail,
                u'password' : password,
                u'birthday' : bd,
                u'genre' : genre,
                u'job' : job,
                u'profile' : uploaded_file_url,
                u'save' : []
            }
            database.add(u'users',mail,data) #add to user , data.id , data
            return render(request,'log.html',{
                "massage":"ลงทะเบียนสำเร็จ"
            })
        else :
            return render(request,'regis.html')

#-----CONSOLE------

def console(request) :
    if request.session.get('auth') :
        return render(request,'console.html',{
            "data" : database.get_doc(u'users',request.session.get('mail')),
            "records" : database.search(u'playing_records',u'creator',request.session.get('auth'))
        })
    else :
        return redirect('/login/')

#-----LOG--------

def log(request,massage) :
    return render(request,'log.html',{
        "massage":massage
    })


#-----VIEW-------

def games(request,game) :
    data = database.search(u'games',u'type',game)
    return render(request,'index.html',{
        "games" : data
    })

#-----RECORD-----
def record(request,id) :
    if request.is_ajax() :
        di = request.GET.get('id')
        player = database.search(u'players',u'dash_id',di)
        return JsonResponse(player ,safe=False)
    else :
        print(id)
        return render(request,'dashboard.html',{
            'id' : id
        })

#-----ERROR------

def notfound_404(request, exception) :
    return render(request,'log.html',{
        "massage":"404 not found"
    })

def error_500(request) :
    return render(request,'log.html',{
        "massage":"500 Error"
    })
