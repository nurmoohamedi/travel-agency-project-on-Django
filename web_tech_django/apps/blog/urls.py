from django.urls import path

from . import views
from django.contrib import admin


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin', admin.site.urls),
]
