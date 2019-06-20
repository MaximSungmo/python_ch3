"""python_ch3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

import helloworld.views as helloworld_views

urlpatterns = [
    path('', helloworld_views.index, name='index'),
    path('test_1/', helloworld_views.test_1),
    path('hello/', helloworld_views.hello),
    path('hello2/<int:id>/', helloworld_views.hello2)

]
