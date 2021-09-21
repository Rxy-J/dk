"""DK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from main.proc import api, getPage

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # 页面
    path("getCode/", getPage.getCodePage),
    path("login/", getPage.getLoginPage),

    # API
    path("api/getcode/", api.getCode),
    path("api/login/", api.login),
    path("api/signin/", api.signIn),
    path("api/getuserinfo/", api.getUserInfo),
    path("api/getrecord/", api.getRecord),
    path("api/getall/", api.getAll),
    path("api/logout/", api.logout),
    # path("api/updatepwd/", api.updatePassword)
]