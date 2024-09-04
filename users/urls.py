from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.registeruser,name='register'),
    path('logout/',views.logoutpage,name='logout'),
    path('login/',views.loginpage,name='login'),
    path('',views.profiles,name='profiles'),
    path('profile/<str:pk>/',views.userprofile,name='user-profiles'),
    path('account/',views.accounts,name='account'),
    path('profile-edit',views.useredit,name='profile-edit'),
    path('create-skill/',views.addskill,name='create-skill'),
    path('update-slill<str:pk>/',views.updateskill,name="update-skill"),

    path('delete-skill<str:pk>/',views.deleteskill,name='delete-skill'),
    path('inbox/',views.inbox,name='inbox'),
    path('message/<str:pk>/',views.viewMessage,name='message'),
    path('send-message/<str:pk>/',views.createMessage,name='create-message')


]
