from django import forms
from .models import (Company,CustomUser, 
                     Transporter, Vehicle, 
                     VehicleOwner, Driver, 
                     VehicleRequest)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

USERTYPE = CustomUser.TYPE


class CustomUserRegistration(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',"phone","UserType","password1","password2")

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email','Address')

class Company_Update_Form(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('Company_Name',)

class Transporter_Update_Form(forms.ModelForm):
    class Meta:
        model = Transporter
        fields = ('pan_card', "aadhar","transport_name","builti_number")

class Driver_Update_Form(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('license', "aadhar")

class Vehicle_Update_Form(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('driver', "vehicle_number","is_vehicle_active")

class BankDetail_Update_Form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('Account_Holder_Name','IFSC','Account_Type','Account_Number','Bank_Name','UPI_QR_CODE')

# ***********************************************************************
# ************************** ADMIN FORMS *********************************************
# ***********************************************************************
class BaseAdminUserTypeForm(UserCreationForm):
    user_type = None  # Placeholder for user type

    def save(self, commit=True):
        if not self.user_type:
            raise ValueError("user_type not set !!!")
        user = super().save(commit=False)
        user.UserType = self.user_type
        user.save()
        return user
    
USERFIELDS  = ('username',"phone")

class AdminCompanyUpdateForm(BaseAdminUserTypeForm):
    user_type = USERTYPE.Company
    class Meta:
        model = Company
        fields = USERFIELDS + ('Company_Name',)

class AdminTransporterUpdateForm(BaseAdminUserTypeForm):
    user_type = USERTYPE.Transporter
    class Meta:
        model = Transporter
        fields = USERFIELDS + ('pan_card', "aadhar","transport_name","builti_number")

class AdminDriverUpdateForm(BaseAdminUserTypeForm):
    user_type = USERTYPE.Driver
    class Meta:
        model = Driver
        fields = USERFIELDS + ('license', "aadhar")
