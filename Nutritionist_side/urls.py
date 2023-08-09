from django.urls import path

from . import views

urlpatterns = [
    path('dashboardNutritionist/', views.index, name='dashboardNutritionist'),
    path('registration/', views.registration, name='registration'),
    path('submitform/', views.sumbitform, name='submitform'),
    path('profile/<str:Email>/', views.profile, name='profile'),
    path('update/<str:Email>/', views.update, name='update'),
    path('addmeeting/', views.addMeeting, name='addmeeting'),
    path('updateprofileNut/', views.updateProfileNut, name='saveUpdate'),
    path('loginNut/', views.loginNut, name='loginNut'),
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('signupNut/', views.signup, name='signupNut'),
    path('signupSubmitNut/', views.signupSubmitNut, name='signupSubmitNut'),
    path('loginSubmitNut/', views.loginSubmitNut, name='loginSubmitNut'),
    path('updateNut/', views.updateNut, name='updateNut'),
    path('profileNut/', views.profileNut, name='profileNut'),
    path('logoutNut/', views.userLogoutNut, name='logoutNut'),
    




    ]