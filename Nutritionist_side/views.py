from django.shortcuts import render,redirect
from django.http import HttpResponse
from polls.models import *
from polls.emailBackend import EmailBackend
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'Nutritionist_side/dashboard.html',{})
def registration(request):
    return render(request,'Nutritionist_side/registor.html',{})
def signup(request):
    return render(request, 'Nutritionist_side/signupNut.html', {})
def signupSubmitNut(request):
    if request.method == 'POST':
        full_name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if (password1 != password2):
            messages.error(request, "password didn't match!")
            return redirect('signupNut')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None

        if (user is not None):
            if (user.email == email):
                messages.error(request, "Email already registered!")
            # return redirect("signup")
            if (user.phone == phone):
                messages.error(request, "Phone # already exist!")

            return render(request, 'Nutritionist_side/signupNut.html', {})

        user = CustomUser(email=email, username=email,
                          phone=phone, user_type='2',first_name=full_name)
        user.set_password(password1)
        user.save()
        return render(request, 'Nutritionist_side/registor.html', {'user':user})

    return render(request, 'Nutritionist_side/success.html', {})

def loginSubmitNut(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = EmailBackend.authenticate(
            request, username=email, password=password)

        if user != None:
            login(request, user)
            request.session['user_id'] = user.email  # type: ignore
            user_type = user.user_type  # type: ignore
            user_name = user.get_username()
            print(request.session['user_id'])
            if user_type == '1':
                return render(request,'polls/dashboard.html',{'user':user})
            elif user_type =='2':
                try:
                    nuttrition=Nutrition.objects.get(Email=request.user.email)
                except Nutrition.DoesNotExist:
                    nuttrition=None
                if nuttrition is None:
                    try:
                        nuttrition_req=Nutrition_Request.objects.get(Email=request.user.email)
                    except Nutrition_Request.DoesNotExist:
                        nuttrition_req=None
                    if nuttrition_req is None:
                        return render(request,'Nutritionist_side/registor.html',{'user':user})
                    else:
                        return render(request,'Nutritionist_side/success.html',{})
                else:
                    user = request.user
                    return render(request,'Nutritionist_side/dashboard.html',{'user':user})
            elif user_type == '3':
                pass
            else:
                messages.error(request, "Email/password are Invalid!")
                return redirect('loginNut')
        else:
            messages.error(
                request, "User Not Found! Enter Correct Email/Password")
            return redirect('loginNut')

        return redirect('loginSubmitNut')

    return redirect('loginNut')
def sumbitform(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        country=request.POST.get('country')
        email=request.POST.get('email')
        phone=request.POST.get('phone_number')
        degree=request.POST.get('degree')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        experience=request.POST.get('experience')
        nutritionist_request=Nutrition_Request(First_name=first_name,Last_name=last_name,Country=country,Email=request.user.email,Phone=phone,Degree=degree,Gender=gender,Address=address,Experience=experience,Password="")
        nutritionist_request.save()
    return render(request,"Nutritionist_side/success.html",{})
def profile(request,Email):
    nut=Nutrition.objects.all().filter(Email=Email).values()
    return render(request,'Nutritionist_side/profile.html',{'item':nut[0]})
def update(request,Email):
    nut=Nutrition.objects.all().filter(Email=Email).values()
    return render(request,'Nutritionist_side/profile_update.html',{'item':nut[0]})
def newMeeting(request):
    return render(request,'Nutritionist_side/meetings.html',{'user':request.user})
def updateProfileNut(request):
    if request.method=="POST":
        Title=request.POST.get('title')
        Name=request.POST.get('name')
        Bio=request.POST.get('bio')
        Email=request.POST.get('email')
        Phone=request.POST.get('phone')
        age=request.POST.get('age')
        Experience=request.POST.get('experience')
        Skill1=request.POST.get('skill1')
        Skill2=request.POST.get('skill2')
        Skill3=request.POST.get('skill3')
        Skill4=request.POST.get('skill4')
        Rate_skill1=request.POST.get('rate_skill1')
        Rate_skill2=request.POST.get('rate_skill2')
        Rate_skill3=request.POST.get('rate_skill3')
        Rate_skill4=request.POST.get('rate_skill4')
        Days_of_Program=request.POST.get('availability')
        Customers=request.POST.get('customers')
        Sessions=request.POST.get('sessions')
        link_Calendly=request.POST.get('link')
        instance=Nutrition.objects.filter(Email=Email).update(Title=Title,Name=Name,Bio=Bio,Email=Email,Phone=Phone,age=age,
                                                              Experience=Experience,Skill1=Skill1,Skill2=Skill2,Skill3=Skill3,Skill4=Skill4,Rate_skill1=Rate_skill1,Rate_skill2=Rate_skill2,Rate_skill3=Rate_skill3,Rate_skill4=Rate_skill4,Days_of_Program=Days_of_Program,Customers=Customers,Sessions=Sessions,link_Calendly=link_Calendly)
        nut=Nutrition.objects.all().filter(Email=Email).values()
        return render(request,'Nutritionist_side/profile.html',{'item':nut[0]})
    return HttpResponse("Profile has been updated")
def loginNut(request):
        return render(request,"Nutritionist_side/login2.html",{})
def addMeeting(request):
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            day=request.POST.get('day')
            start_time=request.POST.get('start_time')
            end_time=request.POST.get('end_time')
            duration=request.POST.get('duration')  
            
            meeting=Meeting(name=name,nutrition=email,day=day,start_time=start_time,end_time=end_time,duration=duration)
            meeting.save()
        return redirect('newMeeting')
@login_required(login_url='/Nutritionist/loginNut/')
def profileNut(request):
    email=request.user.email
    nut=Nutrition.objects.get(Email=email)
    return render(request,'Nutritionist_side/profile.html',{'item':nut})    

@login_required(login_url='/Nutritionist/loginNut/')
def updateNut(request):
    email=request.user.email
    nut=Nutrition.objects.get(Email=email)
    return render(request,'Nutritionist_side/profile_update.html',{'item':nut})    

@login_required(login_url='/Nutritionist/loginNut/')
def userLogoutNut(request):
    logout(request)
    return redirect('loginNut')



        




    

        
