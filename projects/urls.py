from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects,name='project'),
    path('project/',views.projects,name='project'),
    path('project/<str:pk>',views.projectss,name='project'),
    path('projectform',views.createproject,name="createproject"),
    path('update-project/<str:pk>/',views.updateproject,name='update-project'),
    path('delete_template/<str:pk>/',views.deleteproject,name='delete_template')
]
