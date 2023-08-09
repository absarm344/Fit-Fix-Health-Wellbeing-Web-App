from django.shortcuts import render,redirect
from django.http import HttpResponse
from Nutritionist_side.models import *
from polls.models import *
from admin_side.models import *
# Create your views here.
def sideBar(request):
    return render(request,'admin_side/sidebar.html',{})
def list(request):
    user=CustomUser.objects.all().values()
    # nutrition=Nutrition.objects.all().values()
    return render(request,'admin_side/list.html',{'item':user})
def list2(request):
    meeting=Meeting.objects.all().values()
    return render(request,'admin_side/list2.html',{'item':meeting})
def allNutReq(request):
    nutrition=Nutrition_Request.objects.all()
    if nutrition is not None:
        # nutrition=Nutrition_Request.objects.all().values()
        return render(request,'admin_side/list3.html',{'item':nutrition})
    return render(request,'admin_side/list3.html',{}) 

def Packages(request):
    return render(request,'admin_side/package.html',{})
def addNutritionist(request):
    if request.method=="POST":
        myid=request.POST.get('my_id')
        nut=Nutrition_Request.objects.all().filter(id=myid).values()
        myNutrition=Nutrition(Name=nut[0]['First_name']+' '+nut[0]['Last_name'],Email=nut[0]['Email'],Phone=nut[0]['Phone'],Experience=nut[0]['Experience'])
        myNutrition.save()
        nut=Nutrition_Request.objects.filter(id=myid).delete()
    return redirect('allNutReq')
def blockUser(request,Email):
    block=Blocked(Email=Email)
    block.save()
    return redirect("list")
def deleteUser(request,Email):
    if Nutrition.objects.filter(Email=Email)!='null':
        element=Nutrition.objects.filter(Email=Email).delete()
    elif CustomUser.objects.filter(Email=Email)!='null':
        element=CustomUser.objects.filter(email=Email).delete()
    
    return redirect("list")
def deleteReqNut(request,Email):
    element=Nutrition_Request.objects.filter(Email=Email).delete()
    return redirect("allNutReq")


    

