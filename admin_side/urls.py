from django.urls import path

from . import views

urlpatterns = [
    path('sidebar', views.sideBar, name='sidebar'),
    path('', views.list, name='list'),
    path('list2/', views.list2, name='list2'),
    path('allNutReq/', views.allNutReq, name='allNutReq'),
    path('packages/', views.Packages, name='packages'),
    path('blockUser/<str:Email>/', views.blockUser, name='blockuser'),
    path('deleteUser/<str:Email>/', views.deleteUser, name='deleteuser'),
    path('deletereqNut/<str:Email>/', views.deleteReqNut, name='deleteReqNut'),
    path('addnut/', views.addNutritionist, name='addNutritionist'),
    
    
]