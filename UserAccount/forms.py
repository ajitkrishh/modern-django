from django import forms
from .models import (Company,CustomUser, 
                     Transporter, Vehicle, 
                     VehicleOwner, Driver, 
                     VehicleRequest)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

USERTYPE = CustomUser.TYPE

UPDATE_FIELDS = ('first_name', 'last_name', 'email','Address')
ADMIN_UPDATE_FIELDS = ('username','phone','password')
class CustomUserRegistration(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',"first_name","last_name","phone","UserType","password1","password2")

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UPDATE_FIELDS 

class CompanyUpdateForm(UserChangeForm):
    class Meta:
        model = Company
        fields = ('Company_Name',)

class TransporterUpdateForm(UserChangeForm):
    class Meta:
        model = Transporter
        fields = ('pan_card', "aadhar","transport_name","builti_number","vehicle_under_control")

class DriverUpdateForm(UserChangeForm):
    class Meta:
        model = Driver
        fields = ('license', "aadhar")

class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('driver', "vehicle_number","is_vehicle_active")

class BankDetailUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('Account_Holder_Name','IFSC','Account_Type','Account_Number','Bank_Name','UPI_QR_CODE')

# ***********************************************************************
# ************************** ADMIN FORMS *********************************************
# ***********************************************************************

# class AdminCompanyUpdateForm(UserChangeForm):
#     user_type = USERTYPE.Company
#     class Meta:
#         model = Company
#         fields = ('Company_Name',)

# class AdminTransporterUpdateForm(UserChangeForm):
#     user_type = USERTYPE.Transporter
#     class Meta:
#         model = Transporter
#         fields = ('pan_card', "aadhar","transport_name","builti_number")

# class AdminDriverUpdateForm(UserChangeForm):
#     user_type = USERTYPE.Driver
#     class Meta:
#         model = Driver
#         fields = ('license', "aadhar")
