from django.urls import path

from . import views
from django.contrib import admin


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('tours', views.tours, name='tours'),
    path('add_tour', views.addTour, name='add_tour'),
    path('tour/<id>', views.detail_view, name='tour_detail'),
    path('tour/<id>/edit', views.tour_edit, name='tour_edit'),
    path('services', views.services, name='services'),
    path('admin', admin.site.urls),
]
