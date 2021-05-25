from django.contrib import admin
from django.urls import path
from aap import views


urlpatterns = [
    path('',views.index,name='HOME PAGE'),
    path('makeeasy',views.make ,name='home page'),
   path('contact',views.contact ,name='home page'),
   path('about',views.about ,name='home page'),
]


