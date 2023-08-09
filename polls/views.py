from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from polls.emailBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Nutritionist_side.models import Nutrition
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import *
from . import models
from polls.functions import Weight_Gain, Weight_Loss, Healthy
import stripe
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid


def index(request):
    return render(request, 'polls/first.html', {})


def signup(request):
    return render(request, 'polls/signup2.html', {})


def loginn(request):
    return render(request, 'polls/login2.html', {})


def forget(request):
    return render(request, 'polls/forget.html', {})


def success(request):
    return render(request, 'polls/success.html', {})


def signupSubmit(request):
    if request.method == 'POST':
        full_name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if (password1 != password2):
            messages.error(request, "password didn't match!")
            return redirect('signup')

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

            return render(request, 'polls/signup2.html', {})

        user = CustomUser(email=email, username=email,
                          phone=phone, first_name=full_name)
        user.set_password(password1)
        user.save()

    return render(request, 'polls/success.html', {})


def loginSubmit(request):
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
                diet = dietProfileSetting.objects.get(tagE=request.user.email)
                diet_goal = diet.goal
                exers = exercises.objects.filter(goal=diet_goal)
                context = {
                    'exers': exers
                }
                return render(request, 'polls/dashboard.html', context)
            elif user_type == '2':
                pass
            elif user_type == '3':
                pass
            else:
                messages.error(request, "Email/password are Invalid!")
                return redirect('login')
        else:
            messages.error(
                request, "User Not Found! Enter Correct Email/Password")
            return redirect('login')

        return redirect('loginSubmit')

    return redirect('login')


@login_required(login_url='/login/')
def Dashboard(request):
    diet = dietProfileSetting.objects.get(tagE=request.user.email)
    diet_goal = diet.goal
    exers = exercises.objects.filter(goal=diet_goal)
    context = {
        'exers': exers
    }
    return render(request, 'polls/dashboard.html', context)


@login_required(login_url='/login/')
def DietShow(request):
    try:
        diet_def = dietProfileSetting.objects.get(tagE=request.user.email)
        if (diet_def != None):
            if ((diet_def.age == '0' or diet_def.age == '') or (diet_def.weight == '0' or diet_def.weight == '')
                or (diet_def.heightCm == '0' or diet_def.heightCm == '') or (diet_def.waistSize == '0' or diet_def.waistSize == '')
                    or (diet_def.neckSize == '0' or diet_def.neckSize == '') or (diet_def.bfp == '0' or diet_def.bfp == '')):
                messages.error(request, "Update Your data First")
                return redirect('dietProfile')
            else:
                age = int(diet_def.age)
                gender = diet_def.gender
                weight = int(diet_def.weight)
                heightCm = int(diet_def.heightCm)
                neckSize = int(diet_def.neckSize)
                waistSize = int(diet_def.waistSize)
                goal = diet_def.goal
                activity = float(diet_def.activity)
                bfp = float(diet_def.bfp)

                leanfactor = 0.0
                if (gender == "m"):
                    if (10 <= bfp <= 14):
                        leanfactor = 1
                    elif (15 <= bfp <= 20):
                        leanfactor = 0.95
                    elif (21 <= bfp <= 28):
                        leanfactor = 0.90
                    else:
                        leanfactor = 0.85
                else:
                    if (14 <= bfp <= 18):
                        leanfactor = 1
                    elif (19 <= bfp <= 28):
                        leanfactor = 0.95
                    elif (29 <= bfp <= 38):
                        leanfactor = 0.90
                    else:
                        leanfactor = 0.85

                maintaincalories = int(weight*24*leanfactor*activity)
                caloriesreq = 0
                finaldata = []
                bmi = 0
                bmiinfo = ""

                if (goal == "weight gain"):
                    print("wg")
                    finaldata = Weight_Gain(age, weight, heightCm)
                    bmi = int(finaldata[len(finaldata)-2])
                    bmiinfo = finaldata[len(finaldata)-1]
                    caloriesreq = maintaincalories+300
                if (goal == "weight loss"):
                    print("wl")
                    finaldata = Weight_Loss(age, weight, heightCm)
                    bmi = int(finaldata[len(finaldata)-2])
                    bmiinfo = finaldata[len(finaldata)-1]
                    caloriesreq = maintaincalories-300
                if (goal == "healthy"):
                    print("h")
                    finaldata = Healthy(age, weight, heightCm)
                    bmi = int(finaldata[len(finaldata)-2])
                    bmiinfo = finaldata[len(finaldata)-1]
                    caloriesreq = maintaincalories

                breakfastdata = Food.objects.all().filter(bf=1).filter(name__in=finaldata)
                lunchdata = Food.objects.all().filter(lu=1).filter(name__in=finaldata)
                dinnerdata = Food.objects.all().filter(di=1).filter(name__in=finaldata)
                
                print('breakfastdata',breakfastdata)
                print('lunchdata',lunchdata)

                # print(finaldata,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                context = {
                    "breakfast": breakfastdata,
                    "lunch": lunchdata,
                    "dinner": dinnerdata,
                    "bmi": bmi,
                    "bmiinfo": bmiinfo,
                    "caloriesreq": caloriesreq
                }

                recommendDietParams = [age, gender,
                                       neckSize, waistSize, heightCm, weight]
                print(recommendDietParams)
                print(context)
                return render(request, "polls/dietShow.html", context)
        else:
            return redirect('dietProfile')
    except dietProfileSetting.DoesNotExist:
        # Handle the exception here, such as redirecting the user or displaying an error message
        # For example:
        messages.error(request, "Update Diet data first to see diet.")
        return redirect('dietProfile')

    return render(request, 'polls/dietShow.html', {})


@login_required(login_url='/login/')
def userLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def userProfile(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'polls/profile.html', context)


@login_required(login_url='/login/')
def dietProfile(request):
    diet_Parmas = dietProfileSetting.objects.filter(tagE=request.user.email)
    if diet_Parmas is None or diet_Parmas.count() == 0:
        diet_Parmas = dietProfileSetting()
        diet_Parmas.tagE = request.user.email
        diet_Parmas.save()
    else:
        diet_Parmas = dietProfileSetting.objects.get(tagE=request.user.email)
    context = {
        'diet_Parmas': diet_Parmas
    }
    return render(request, "polls/diet_profile.html", context)


@login_required(login_url='/login/')
def dietUpdate(request):
    email = request.user.email

    if request.method == "POST":
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        weight = request.POST.get('weightKg')
        heightCm = request.POST.get('hcm')
        neckSize = request.POST.get('neckSize')
        waistSize = request.POST.get('waistSize')
        goal = request.POST.get('goal')
        activity = request.POST.get('activity')
        bfp = request.POST.get('bfp')

        try:
            if dietProfileSetting.objects.get(tagE=email) is None:
                if (age != None or age != '' or gender != None or gender != '' or weight != None or weight != '' or
                    heightCm != None or heightCm != '' or neckSize != None or neckSize != '' or waistSize != None or waistSize != '' or
                   goal != None or goal != '' or activity != None or activity != '' or bfp != None or bfp != ''):
                    dietProf = dietProfileSetting(tagE=email, age=age, gender=gender, weight=weight, heightCm=heightCm, neckSize=neckSize,
                                                  waistSize=waistSize, goal=goal, activity=activity, bfp=bfp)
                    dietProf.save()
                    messages.success(request, 'Profile Saved Successfully!')
                    return redirect('dietProfile')
                else:
                    messages.error(request, 'All parameters are required')
                return redirect('dietProfile')
            else:
                dietProf = dietProfileSetting.objects.get(tagE=email)
                dietProf.age = age
                dietProf.gender = gender
                dietProf.weight = weight
                dietProf.heightCm = heightCm
                dietProf.neckSize = neckSize
                dietProf.waistSize = waistSize
                dietProf.goal = goal
                dietProf.activity = activity
                dietProf.bfp = bfp
                dietProf.save()
                messages.success(request, 'Profile Updated Successfully!')
                return redirect('dietProfile')

        except:
            messages.error(request, 'Failed to Update')
            return redirect('dietProfile')

    return render(request, "polls/diet_profile.html")


@login_required(login_url='/login/')
def profileUpdate(request):

    if request.method == 'POST':
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        try:
            customUser = CustomUser.objects.get(id=request.user.id)
            customUser.first_name = first_name
            customUser.last_name = last_name
            customUser.phone = phone
            print(profile_pic)
            if profile_pic is not None:
                unique_filename = str(uuid.uuid4()) + \
                    '.' + profile_pic.name.split('.')[-1]
                print(unique_filename)
                image_path = default_storage.save(
                    'media/profile_pic/' + unique_filename, ContentFile(profile_pic.read()))
                # Save the image path to the user's profile_pic field
                print(image_path)
                customUser.profile_pic = image_path
                print(customUser.profile_pic)
            customUser.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('userProfile')
        except:
            messages.error(request, 'Failed to Update Your Profile!')

    return render(request, "polls/profile.html")


def events(request):
    return render(request, 'polls/events.html', {})


def subscription(request):
    subs = subPlan.objects.all()
    return render(request, 'polls/subscription.html', {'subs': subs})


def checkout(request):
    sub_title = request.GET.get('sub_title')
    sub_price = request.GET.get('sub_price')

    if sub_title != 'NULL' and sub_price != 0:
        request.session['sub_title'] = sub_title
        request.session['sub_price'] = sub_price
    # print(sub_title, sub_price)
    return render(request, 'polls/checkout.html', {'sub_title': sub_title, 'sub_price': sub_price})


stripe.api_key = 'sk_test_51NTsCzSCN1dWKbv0yoIRmSWwueY3KwaeuODKYqFKZUBXSTMbBnRatULoLSujTX7O0LksbmXJcuYC90ZplJKJyA9H00ivOg6Ofo'


def cardSubmit(request):
    # sub_title = str(request.session.get('sub_title'))
    # sub_price = int(request.session.get('sub_price'))
    # print(sub_title,sub_price)
    sub_title = ""
    sub_price = 0
    if request.session.get('sub_title') == "Basic Tier":
        sub_title = 'Basic Tier'
        sub_price = 1400
    elif request.session.get('sub_title') == "Premium Tier":
        sub_title = 'Premium Tier'
        sub_price = 4000
    elif request.session.get('sub_title') == "VIP Tier":
        sub_title = 'VIP Tier'
        sub_price = 7000

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'pkr',
                'product_data': {
                    'name': sub_title,
                },
                'unit_amount': sub_price*100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout_success/',
        cancel_url='http://127.0.0.1:8000/checkout_failed/',
    )

    return redirect(session.url, code=303)


def History(request):
    return render(request, 'polls/Activity_History.html', {})


def singleVideo(request):
    return render(request, 'polls/single-video.html', {})


def checkout_success(request):
    return render(request, 'polls/checkout_success.html', {})


def checkout_failed(request):
    return render(request, 'polls/checkout_failed.html', {})


def profile(request, Email):
    nut = Nutrition.objects.all().filter(Email=Email).values()
    return render(request, 'polls/profileN.html', {'item': nut[0]})


def ourTeam(request):
    team = Nutrition.objects.all().values()
    return render(request, 'polls/our-team.html', {'item': team})


def bmiCalc(request):
    return render(request, "polls/bmi_calculator.html", {})


def BMRCalc(request):
    return render(request, 'polls/BMR.html', {})
