from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'), #Main
    path('<str:string>/', views.redir, name="redir"), #Redirect
]