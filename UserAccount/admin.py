from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# from .models import *
from .models import (Company,CustomUser, 
                     Transporter, Vehicle, 
                     VehicleOwner, Driver, 
                     VehicleRequest)

class CustomUserAdmin(UserAdmin):
    list_display = ['username','phone','get_full_name',
                    'UserType','credit']
    list_filter = ['UserType']
    list_per_page = 20
    search_fields= ['phone']
    
admin.site.register(CustomUser,CustomUserAdmin)

class Transporter_Admin(admin.ModelAdmin):
    list_display = ['id','transport_name','builti_number']
    list_per_page = 20
    list_editable = ['transport_name']
admin.site.register(Transporter,Transporter_Admin)


class Company_Admin(admin.ModelAdmin):
    list_display = ['id','Company_Name']
    list_editable = ['Company_Name']
    list_per_page = 20

admin.site.register(Company,Company_Admin)

class Driver_Admin(admin.ModelAdmin):
    list_display = ['id','license','aadhar']
    list_per_page = 20
    list_editable = ['license','aadhar']
admin.site.register(Driver,Driver_Admin)


class VehicleOwner_Admin(admin.ModelAdmin):
    list_display = ['id']
    list_per_page = 20
admin.site.register(VehicleOwner,VehicleOwner_Admin)

class Vehicle_Admin(admin.ModelAdmin):
    list_select_related = ['owner']
    list_display = ['id','vehicle_number','owner','driver']
    search_fields= ['vehicle_number']
    list_per_page = 20
admin.site.register(Vehicle,Vehicle_Admin)


class Vehicle_Requests_Admin(admin.ModelAdmin):
    list_select_related = ['vehicle' , 'transporter' , 'vehicle_owner']
    list_display = ['id','vehicle' , 'transporter' , 'vehicle_owner','request_status']
    list_editable = ['request_status']
    list_per_page = 20
admin.site.register(VehicleRequest,Vehicle_Requests_Admin)
