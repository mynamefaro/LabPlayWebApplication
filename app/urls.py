"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import play
from . import methods
from . import mobile
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.default),
    path('index/',views.index,name="index"),
    path('games/play/<slug:id>/',play.index,name="play"),
    path('like/<slug:id>/',play.like,name="like"),
    path('finish/<slug:id>/',play.finish,name="finish"),
    path('dashboard/<slug:id>/',play.dashboard,name="dashboard"),
    path('record/<slug:id>/',views.record,name="record"),
    path('login/',views.login,name="login"),
    path('contact/',views.contact,name="contact"),
    path('regis/',views.regis,name="regis"),
    path('search/',views.search,name="search"),
    path('console/',views.console,name="console"),
    path('logout/',methods.logout,name="logout"),
    path('dataview/',methods.logout,name="dataview"),
    path('games/<slug:game>',views.games,name="games"),
    path('log/<slug:massage>',views.log,name="log")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app.views.notfound_404'
handler500 = 'app.views.error_500'
