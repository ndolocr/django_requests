from django.urls import path

from xml_requests import views

urlpatterns = [
    path('get/project/name', views.get_project_name, name='get_project_name'),
]