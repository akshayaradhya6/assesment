"""
URL configuration for transportpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from transportapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
   
    path('question_list', views.question_list, name='question_list'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/post/', views.post_question, name='post_question'),
    path('question/<int:question_id>/answer/', views.post_answer, name='post_answer'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
]
