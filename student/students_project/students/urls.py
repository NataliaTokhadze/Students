from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_page, name='students'),
    path('', views.main_page, name='main')
]