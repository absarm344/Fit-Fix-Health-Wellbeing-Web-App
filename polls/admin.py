from django.contrib import admin
from .models import *
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

# class UserModel(UserAdmin):
#     list_display = ['username','user_type']

admin.site.register(CustomUser)
admin.site.register(dietProfileSetting)

class subPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','feature1','feature2','feature3','feature4','feature5')
admin.site.register(models.subPlan, subPlanAdmin)

class exerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'desc','link','goal')
admin.site.register(models.exercises, exerciseAdmin)

