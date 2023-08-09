from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginn, name='login'),
    path('forget/', views.forget, name='forget'),
    path('success/', views.success, name='success'),
    path('events/', views.events, name='events'),

    path('subscription/', views.subscription, name='subscription'),
    path('checkout/', views.checkout, name='checkout'),

    path('cardSubmit/', views.cardSubmit, name='cardSubmit'),

    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('checkout_failed/', views.checkout_failed, name='checkout_failed'),
    path('cardSubmit/', views.cardSubmit, name='cardSubmit'),
    path('signupSubmit/', views.signupSubmit, name='signupSubmit'),
    path('loginSubmit/', views.loginSubmit, name='loginSubmit'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('dietshow/', views.DietShow, name='dietShow'),
    path('bmiCalc/', views.bmiCalc, name='bmiCalc'),
    path('BMRCalc/', views.BMRCalc, name='BMRCalc'),
    path('profile/<str:Email>/', views.profile, name='profileN'),
    path('our-team/', views.ourTeam, name='ourteam'),

    path('userLogout/', views.userLogout, name='userLogout'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('dietProfile/', views.dietProfile, name='dietProfile'),
    path('profileUpdate/', views.profileUpdate, name='profileUpdate'),
    path('dietUpdate/', views.dietUpdate, name='dietUpdate'),
    path('history/', views.History, name='history')

]
