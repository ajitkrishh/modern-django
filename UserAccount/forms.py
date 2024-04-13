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
class BaseAdminUserTypeForm(UserCreationForm):
    user_type = None  # Placeholder for user type

    def save(self, commit=True):
        if not self.user_type:
            raise ValueError("user_type not set !!!")
        user = super().save(commit=False)
        user.UserType = self.user_type
        user.save()
        return user
    

class AdminCompanyCreateForm(BaseAdminUserTypeForm):
    user_type = USERTYPE.Company
    class Meta:
        model = Company
        fields = ('Company_Name',)


class AdminTransporterCreateForm(BaseAdminUserTypeForm):
    user_type = USERTYPE.Transporter
    class Meta:
        model = Transporter
        exclude = ('password', )
        fields = ADMIN_UPDATE_FIELDS + UPDATE_FIELDS + ('pan_card', "aadhar","transport_name","builti_number")

class AdminDriverCreateForm(BaseAdminUserTypeForm):
    user_type = USERTYPE.Driver
    class Meta:
        model = Driver
        exclude = ('password', )
        fields = ADMIN_UPDATE_FIELDS + UPDATE_FIELDS + ('license', "aadhar")

class AdminCompanyUpdateForm(UserChangeForm):
    user_type = USERTYPE.Company
    class Meta:
        model = Company
        fields = ADMIN_UPDATE_FIELDS + UPDATE_FIELDS + ('Company_Name',)

class AdminTransporterUpdateForm(UserChangeForm):
    user_type = USERTYPE.Transporter
    class Meta:
        model = Transporter
        fields = ADMIN_UPDATE_FIELDS + UPDATE_FIELDS + ('pan_card', "aadhar","transport_name","builti_number")

class AdminDriverUpdateForm(UserChangeForm):
    user_type = USERTYPE.Driver
    class Meta:
        model = Driver
        fields = ADMIN_UPDATE_FIELDS + UPDATE_FIELDS + ('license', "aadhar")
