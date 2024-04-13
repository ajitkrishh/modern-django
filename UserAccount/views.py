import base64
import datetime
from io import BytesIO
import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.functions import Concat , ExtractMonth
from django.db.models import Exists, OuterRef, Q, Value,F, Sum,Count
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect



from .forms import (CustomUserRegistration, CustomUserUpdateForm, 
                    CompanyUpdateForm, TransporterUpdateForm,
                    DriverUpdateForm, VehicleUpdateForm, BankDetailUpdateForm)

from UserAccount.utils import get_allowed_friendship, get_usertypes, sanitize_integer_values, values_list_to_values
from .models import *

# Create your views here.
USERTYPE = get_usertypes()

class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        print(self.request.user.UserType)
        return reverse("index")
        if self.request.user.UserType == USERTYPE[0]:
            return reverse("organisation-action")
        elif self.request.user.UserType == USERTYPE[1]:
            return reverse("transporter-action")
        elif self.request.user.UserType == USERTYPE[2]:
            return reverse("owner-action")
        elif self.request.user.UserType == USERTYPE[3]:
            return reverse("driver-action")


@login_required
def index(req):     #home.html
    user = req.user
    utype = user.UserType
    for i,model in enumerate([Company, Transporter, VehicleOwner, Driver]):
        objs = []
        for j in range(5):
            username = f'Ajit{i}{j}{i*j}'
            user = model(
                username = username,
                email = f"{str(model).lower()}{j}@c.com",
                UserType = i+1,
                first_name = username,
                last_name = "singh"
            )
            user.set_password("123")
            objs.append(user)
        model.objects.bulk_create(objs)

    # print(dir(user))
    return render(req, "common/index.html")
'''
    today = datetime.datetime.today()
    if utype == USERTYPE[0]:
       
        o_user:Organisation = user.organisation

        linked_transporters = o_user.linked_transporters.values_list("user__id", "transport_name")
        linked_organisations = o_user.linked_Organisation.values_list("id", "Organisation_Name", "user__id")

            
        total_trips = Builti.objects.filter(
                (Q(From=o_user) | Q(To=o_user)) & (Q(Dateloaded__month=today.month)))

        total_trips = total_trips.aggregate(
            rejected_trip=Count('id', filter=Q(status='Rejected')),
            open_trip=Count('id', filter=Q(Dateloaded__month=today.month, status='Open')),
            total_trips=Count('id'),
            total_vehicle=Count('Vehicle', distinct=True),
            monthly_trips=Count('id', filter=Q(DateUnloaded__month=today.month)),
            estimated_turnover=Sum(F('Weight_At_loading') * F('Price_To_Organisation'), 
                                   filter=Q(DateUnloaded__month=today.month), 
                                   output_field=models.DecimalField()),
            estimated_material=Sum(F('Weight_At_loading') ,
                                   filter= Q(DateUnloaded__month=today.month), 
                                   output_field=models.DecimalField())
                                )
        chart_data = Builti.objects.filter(From=req.user.organisation).annotate(
                        month=ExtractMonth('Dateloaded')
                        ).values('month').annotate(count=Count('id')).order_by('month').values('month','count')
        chart_data  =json.dumps(list(chart_data))
        total_trips = sanitize_integer_values(total_trips)

        total_trips['success_trip'] = total_trips["monthly_trips"] - total_trips["rejected_trip"] 
        # print(total_trips)

        linked_organisations = [ {'id':i[0] , 'title': i[1], 'user_id':i[2]}   for i in linked_organisations] 
        linked_transporters = [ {'id':i[0] , 'title': i[1] }   for i in linked_transporters] 
        context = {
            "linked_organisations": linked_organisations,
            "linked_transporters" : linked_transporters,
            "trip" : total_trips,
            'monthly_counts':chart_data
        }

        return render(req, "organisation/home.html", context)

    elif utype == USERTYPE[1]:

        t_user: Transporter = user.transporter

        # Get the IDs and names of all linked organizations for the transporter
        linked_organisations = t_user.Linked_Organisation.values_list(
            'user_id', 'Organisation_Name')
        linked_owners = t_user.vehicle_under_control.values_list(
            'owner__user_id', 'owner__user__first_name').distinct()
        
                
        total_trips = Builti.objects.filter(Transporter=t_user, Dateloaded__month=today.month)
        trip_counts = total_trips.aggregate(
            rejected_trip=Count('id', filter=Q(status='Rejected')),
            open_trip=Count('id', filter=Q(status='Open')),
            total_trips=Count('id'),
            monthly_trips=Count('id', filter=Q(DateUnloaded__month=today.month)),
            estimated_rev=Sum(F('Price_To_Transporter') * F('Weight_At_unloading'), filter=Q(DateUnloaded__month=today.month), 
                              output_field=models.DecimalField())
                              )

        total_trips_count = trip_counts['total_trips']
        monthly_trips_count = trip_counts['monthly_trips']
        rejected_trip = trip_counts['rejected_trip']
        estimated_rev = trip_counts['estimated_rev'] or 0
        open_trip = trip_counts['open_trip'] or 0
        success_trip = monthly_trips_count - rejected_trip
        del trip_counts

        total_vehicle_status = VehicleRequest.objects.filter(Transporter=t_user).aggregate(
                active=Count('id', filter=Q(VehicleStatus=True , request_status='A')),
                inactive=Count('id', filter=Q(VehicleStatus=False,request_status='A')),
                Vehicle_requests=Count('id', filter=Q(request_status='P'))
)
        total_vehicle_status = sanitize_integer_values(total_vehicle_status)
        # print(total_vehicle_status)

        linked_organisations = [ {'id':i[0] , 'title': i[1]}   for i in linked_organisations] 
        linked_owners = [ {'id':i[0] , 'title': i[1]}   for i in linked_owners] 
        context = {
                   "linked_organisations": linked_organisations,
                   "linked_owners": linked_owners,
                   "UserType": utype,
                   "v_data": total_vehicle_status,
                   "trip_data": [total_trips_count, monthly_trips_count, rejected_trip, estimated_rev, success_trip , open_trip]
                   }
        
        return render(req, 'transporter/home.html', context)

    elif utype == USERTYPE[2]:
        
        o_user = user.owner
        vehicle_list = Vehicle.objects.filter(owner__id = o_user.id)   \
                                            .select_related("driver")  \
                                            .values_list('id' , 'vehicle_number',"is_active",'driver__id','driver__user__first_name')


        linked_transporters = VehicleRequest.objects.filter(Vehicle_Owner__id = o_user.id)\
                                    .select_related("Transporter")\
                                        .values_list("Transporter__id","Transporter__Transport_Name").distinct()
        
        active,inactive,no_driver = 0,0,0
        vehicle_id_list = [i[0] for i in vehicle_list]
        for i in vehicle_list:
            if i[2]:
                active+=1
            else:
                inactive +=1
            if not i[3]:
                no_driver +=1
                
        linked_transporters = values_list_to_values(linked_transporters , ['id','title'])

        trips = Builti.objects.filter(Vehicle__in = vehicle_id_list).aggregate(
            rejected_trip=Count('id', filter=Q(status='Rejected')),
            open_trip=Count('id', filter=Q(status='Open')),
            total_trips=Count('id'),
            monthly_trips=Count('id', filter=Q(DateUnloaded__month=today.month)),
            estimated_rev=Sum(F('Price_To_Owner') * F('Weight_At_unloading'), 
                              filter=Q(DateUnloaded__month=today.month), 
                              output_field=models.DecimalField())
            )
        
        trips = sanitize_integer_values(trips)
        trips['success_trip'] = trips["monthly_trips"] - trips["rejected_trip"] 

        vehicle_key_list = ['id', 'title', 'active', 'driver_id', 'driver_name']
        vehicle_list = values_list_to_values(vehicle_list , vehicle_key_list)
        del vehicle_key_list
        
        context = {
            "vehicle_list" : vehicle_list,
            "linked_transporters":linked_transporters,
            "trip":trips,
            "v_data":[active,inactive , no_driver]
        }
        print(context)
        return render(req, "owner/home.html", context)

    elif utype == USERTYPE[3]:
        user_info = user.driver
        additional_info = None
        return render(req, "driver/home.html", {'data': {"userdata": user, 'user_info': user_info, "additional_info": additional_info, "UserType": utype}})
'''


def registration(req):
    if req.method == "POST":
        form = CustomUserRegistration(req.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

        else:  # if invaid form
            for field_errors in form.errors.values():
                    for error in field_errors:
                        messages.error(req, error)
            form = CustomUserRegistration(req.POST)
            return redirect('register')

    elif req.method == "GET":
        form = CustomUserRegistration()
        return render(req, "registration/registration.html", {"form": form})


@login_required
def update_profile(req, pk=None):
# def update_profile(req, pk):
    request_UserType = req.user.UserType
    specfic_usertype_form_class = {
        USERTYPE[0]: CompanyUpdateForm,
        USERTYPE[1]: TransporterUpdateForm,
        USERTYPE[3]: DriverUpdateForm,
    }
    # return render(req, "company/index.html")
    if req.method == "POST":
        form_type = req.POST.get('type')
        if form_type == 'general':
            form_obj = CustomUserUpdateForm(req.POST, instance=req.user)
        elif form_type == 'specific':
            form_obj = specfic_usertype_form_class.get(request_UserType , None)
            if (request_UserType == USERTYPE[0]):
                form_obj = form_obj(
                    req.POST, instance=req.user)

            elif (request_UserType == USERTYPE[1]):
                form_obj = form_obj(
                    req.POST, instance=req.user)

            elif (request_UserType == USERTYPE[2]):
                form_obj = form_obj(req.POST, instance=req.user)
        
        elif form_type == 'bank':
            img_base64 = req.POST.get('compressed_image')
            if img_base64:
                mutable_file = req.FILES.copy()
                image_data = base64.b64decode(img_base64[img_base64.find('base64') + 7:])
                image_name = req.user.username + '.jpg'
                image_file = InMemoryUploadedFile(
                    BytesIO(image_data),  # Pass the image data as BytesIO stream
                    None,  # Set field_name to None
                    image_name,  # Provide a name for the file
                    'image/jpg',  # Set the content type of the file
                    len(image_data),  # Specify the file size
                    None,  # Set the content_type_extra argument to None
                    None  # Set the charset argument to None
                )
                mutable_file['UPI_QR_CODE'] = image_file
                form_obj = BankDetailUpdateForm(req.POST,mutable_file , instance=req.user.account)
    
        if form_obj.is_valid():
            form_obj.save()
        else:
            for field_errors in form_obj.errors.values():
                    for error in field_errors:
                        messages.error(req, error)
        return redirect("update" , pk=req.user.id)
    elif req.method == "GET":
        print(request_UserType)
        # form_obj = specfic_usertype_form_class.get(request_UserType , None)
        form_obj = TransporterUpdateForm()
        bank_detail = BankDetailUpdateForm(instance=req.user)
        return render(req, "userprofile/userform.html", {"bank": bank_detail,'form' : form_obj})


@login_required
def add_vehicle(req):
    user = req.user
    # handle other users .
    if user.UserType == USERTYPE[2]:
        # print(req.__dict__)
        o_user = get_object_or_404(Owner, user=user)
        if req.method == 'POST':
            request_type = req.POST.get('type')
            # if request_type is 1 i.e. to add 
            if request_type == '1' : 
                vh_no = req.POST.get('vh_no')
                driver = req.POST.get('driver')
                # // vlidate the vehicle number format...
                driver_user = CustomUser.objects.filter(username = driver).first()
                if not driver_user:
                    messages.error(req , 'No such driver exists, please register the driver !!!')
                    return render(req , 'vehicle/add_vehicle.html')
                driver = driver_user.driver

                counts = Vehicle.objects.aggregate(
                    driver = Count('id' , filter=Q(driver = driver)),
                    vehicle = Count('id' , filter=Q(vehicle_number = vh_no))
                )
                print(counts)
                msg = ''
                if counts['driver'] == 0:
                    if counts['vehicle'] == 0:
                        new_vehicle = Vehicle.objects.create(
                            owner =  o_user,
                            driver = driver,
                            vehicle_number = vh_no,
                            is_active = False
                        )
                        msg = f'vehicle with number {vh_no} is added successfully !!!'
                    else:
                        msg = 'Vehicle is already registered !!!'
                else:
                    msg = 'Driver is already linked with other vehicle !!!'
                messages.error(req , msg)
                return render(req , 'vehicle/add_vehicle.html')
                
            elif request_type == '2':      # if request_type is 2  i.e delete

                vehicle_id =  req.POST.get('delete_form')
                vehicle = Vehicle.objects.filter(id = vehicle_id , owner_id = o_user.id)
                if vehicle:
                    vehicle = vehicle[0]
                    vehicle.delete()
                    msg = 'Vehicle removed successfully !!!'
                    messages.success(req , msg)
                return render(req , 'vehicle/see_vehicles.html')
        
        elif req.method == 'GET':
            driver_list = Vehicle.objects.filter(owner = req.user.owner).values_list('driver_id','driver__user__first_name' )
            # .values_list('pk','user__first_name' )
            print(driver_list)
            return render(req , 'vehicle/add_vehicle.html', {
                'driver_list' : driver_list
            })
    else:
        messages.error(req , 'Action Not Allowed !!! ')
        return reverse('home')

       


@login_required
def get_vehicle(req):
    user = req.user
    usertype = user.UserType
    print(usertype)
    if (usertype == USERTYPE[0]):
        print('redirecting 1')
        return redirect('home')
    if usertype == USERTYPE[2]:
        owner = user.owner
        vehicle_info = Vehicle.objects.filter(owner=owner).select_related('driver__user').prefetch_related('transporters').values_list(
             'pk',
            "vehicle_number", 
            "transporters__Transport_Name",
            "driver__user__first_name", 
            'is_active').order_by('vehicle_number')
        # print(vehicle_info)

        vehicle_info = values_list_to_values(vehicle_info , ['obj_id','vehicleNumber','stakeholder',
                                                            'driver','status' ])
        context = {
            "vehicle_list":vehicle_info
        }
        return render(req, "vehicle/see_vehicles.html", context)
    
    elif usertype == USERTYPE[1]:
        user = req.user
        transporter = user.transporter
        vehicle_info = VehicleRequest.objects.filter(Transporter_id=transporter.id,
                                                     request_status='A').values_list(
                       'pk',                                 
                      "Vehicle__Vehicle_Number","Vehicle_Owner__user__first_name",
                      "Vehicle__driver__user__first_name","VehicleStatus").order_by('Vehicle')
        
        vehicle_info = values_list_to_values(vehicle_info , ['obj_id','vehicleNumber','stakeholder',
                                                            'driver','status' ])
        context = {
            "vehicle_list":vehicle_info
        }
        print(context)
        return render(req, "vehicle/see_vehicles.html", context)
    
    elif usertype == USERTYPE[3]:
       
        vehicle_info = Vehicle.objects.filter(driver__user_id  = req.user.id).select_related('owner').values_list('pk','owner__user__first_name' , 'is_active','vehicle_number')
        if not vehicle_info:
            return redirect('home')
        
        vehicle_info = values_list_to_values(vehicle_info , [
            'obj_id','stakeholder','status','vehicleNumber'
        ])
        context = {'vehicle_list': vehicle_info}
        print(context)
        return render(req , "vehicle/see_vehicles.html", context)
    else:
        print('redirecting 2')
        return HttpResponseRedirect(reverse('home'))



@login_required
def activate_deacticate_vehicle(req):
    user:CustomUser = req.user
    credit = user.credit
    if req.user.UserType == USERTYPE[1]:  # is transporter
        if req.method == 'POST':
            vehicle_activate_request_id = req.POST.get("vehicle_form")
            operation_type = req.POST.get("operation")
            vehicle_activate_request_obj = get_object_or_404(
                VehicleRequest, pk=vehicle_activate_request_id, Transporter = user.transporter)
            if vehicle_activate_request_obj : 
                if operation_type == 'Activate' and not vehicle_activate_request_obj.VehicleStatus:
                    available_credits = credit
                    if available_credits < 1:
                        messages.warning( req, "Not Enough Credits, Please Buy Some!!! " )
                        print("unable to activate")
                    else:
                        # use some lock here
                        vehicle_activate_request_obj.VehicleStatus = True
                        user.credit -=1
                        vehicle_activate_request_obj.save()
                        user.save()
                        messages.success(req, "Vehicle Activated!!! ")
                elif operation_type == 'Deactivate' and vehicle_activate_request_obj.VehicleStatus:
                    vehicle_activate_request_obj.VehicleStatus = False
                    vehicle_activate_request_obj.save()
                    messages.success(req, "Vehicle Deactivated!!! ")
            else:
                messages.error(req, "Invalid Operation !!! ")
    return redirect(reverse('vehicles'))


@login_required
def build_network(req, id=None):
    search_result_user = []
# assuming user is the current authenticated user
    user = req.user
    usertype = user.UserType
    allowed_friendship = get_allowed_friendship()
    if req.method == 'POST':     #when user search a name 
        # print(req.POST)
        search_str = req.POST.get("search_user", None)
        search_result_user = CustomUser.objects.filter(
            Q(username__icontains=search_str) |
            Q(first_name__icontains=search_str) |
            Q(last_name__icontains=search_str) |
            Q(UserType__icontains=search_str)
        )        
        try:
            search_result_user = search_result_user.filter(UserType__in = allowed_friendship[usertype])
        except:
            search_result_user = []
        print(search_result_user)

        if search_result_user.exists():
            friendships = Friendship.objects.filter(Q(from_user=user) | Q(to_user=user))\
                                            .values('from_user', 'to_user', 'status')
            
            search_result_user = search_result_user.annotate(
                is_friend=Exists(
                    friendships.filter(
                        Q(from_user=OuterRef('pk'), to_user=user) |
                        Q(from_user=user, to_user=OuterRef('pk'))
                    )),
                get_full_name=Concat('first_name', Value(' '), 'last_name')
            )
            search_result_user = search_result_user.filter(~Q(pk=user.pk))\
                                                    .values("pk", "is_friend", "UserType", "get_full_name")
        # print(search_result_user)
    
    elif req.method == "GET":
        if id:          # a get request fires when a connect request is made by user for another user , id refers to the to_user 
            to_User = get_object_or_404(CustomUser, pk=id)
            to_User_usertype = to_User.UserType
            is_allowed = to_User_usertype in  allowed_friendship[usertype]
            if is_allowed:
                new_friend = Friendship.objects.create(
                    from_user=user,
                    to_user=to_User,
                    status='P'
                )
                messages.success(req , 'Connection request made successfully !!!')
                # print(new_friend)
            else:
                messages.warning(req , "Operation not allowed !!!")
    return render(req, "common/explore.html", {'results': search_result_user})


def connection_requests(req):
    user:CustomUser = req.user
    usertype = user.UserType
    if req.method == 'GET':
        connection_request = Friendship.objects.filter(to_user = user.id , status = 'P')\
                                                .select_related('from_user')\
                                                    .values_list('pk','from_user__id' ,'from_user__username','from_user__UserType' )
        connection_request = values_list_to_values(source= connection_request, key_list=['pk' , 'userid','username' , 'usertype'])
        
        context = {'connections':connection_request,"request_type":'user'}
        return render(req , 'common/connection_request.html' , context)
    elif req.method == 'POST':
        # print(req.POST)
        # it is ajax post request, 
        user_decision_type = req.POST.get('type')  # 1 for accept ,  2 for reject
        from_user_id =  req.POST.get('temp')
        friendship_obj_id = req.POST.get('obj')
        friendship_obj:Friendship = get_object_or_404(Friendship ,pk= int(friendship_obj_id))
        from_user = get_object_or_404(CustomUser , pk = from_user_id)
        if user_decision_type not in {'1' , '2'}:
            messages.error(req , "Operation not valid !!!")
            return redirect('home')
        if friendship_obj.from_user_id != int(from_user_id) or friendship_obj.to_user_id != req.user.id:
            messages.error(req , "Operation not valid !!!")
            return redirect('home')
        if friendship_obj.status != 'P':
            messages.error(req , "Operation not valid !!!")
            return redirect('home')
        if user_decision_type == '1':
            from_user_usertype = from_user.UserType
            if from_user_usertype in  get_allowed_friendship()[usertype] :
                if usertype == USERTYPE[0]:
                    if from_user_usertype == USERTYPE[0]:
                        user.organisation.linked_Organisation.add(from_user.organisation)
                    elif from_user_usertype == USERTYPE[1]:
                        from_user.transporter.Linked_Organisation.add(user.organisation)
                elif usertype == USERTYPE[1]:
                    if from_user_usertype == USERTYPE[0]:
                        user.transporter.Linked_Organisation.add(from_user.organisation)
                elif usertype == USERTYPE[2]:
                    if from_user_usertype == USERTYPE[3]:
                        user.owner.linked_driver.add(from_user.driver)
                elif usertype == USERTYPE[3]:
                    if from_user_usertype == USERTYPE[2]:
                        from_user.owner.linked_driver.add(user.driver)
            friendship_obj.status = 'A'
        
        elif user_decision_type == '2':
            friendship_obj.status = 'D'
        friendship_obj.save()
        return HttpResponse('OK')

def vehicle_connection_request(req):
    '''
    method is from transporter only , where he/she rather accept a vehicle request or cancel a request. 
    '''
    user:CustomUser = req.user
    usertype = user.UserType
    
    if usertype != USERTYPE[1]:
        messages.error(req , "Operation not valid !!!")
        return redirect('home') 
    t_user:Transporter = user.transporter
    if req.method == 'GET':
        vh_connection_request = VehicleRequest.objects.filter(Transporter = t_user , request_status = 'P')\
                                                .select_related('vehicle_owner','Vehicle')\
                                                    .values_list('pk','Vehicle_Owner__id' ,'Vehicle_Owner__user__username','Vehicle__id','Vehicle__Vehicle_Number' )
        vh_connection_request = values_list_to_values(source= vh_connection_request, key_list=['pk' , 'ownerid','username' , 'vehicle_id','vehicle_number'])
        
        context = {'connections':vh_connection_request , "request_type":'vehicle'}
        return render(req , 'common/connection_request.html' , context)
    elif req.method == 'POST':
        print(req.POST)
        # it is ajax post request, 
        try:
            user_decision_type = int(req.POST.get('type'))  # 1 for accept ,  2 for reject
            vh_owner_id =  int(req.POST.get('temp'))
            request_vh_id =  int(req.POST.get('temp2'))
            vehicle_req_obj_id = int(req.POST.get('obj'))
        except:
            # redirect('home')
            HttpResponseBadRequest("Not Allowed !!!")
        vehicle_req_obj : VehicleRequest = get_object_or_404(VehicleRequest , pk = vehicle_req_obj_id)
        vehicle : Vehicle = get_object_or_404(Vehicle , pk=request_vh_id)
        # print(vehicle_req_obj.__dict__ )
        if (vehicle_req_obj.Vehicle_Owner_id != vh_owner_id or
            vehicle.owner_id != vh_owner_id):
            # print("11111")
            return redirect('home')
        if user_decision_type == 1:
            vehicle_req_obj.request_status = 'A'
        elif user_decision_type == 2:
            vehicle_req_obj.request_status = 'D'
        # print(vehicle_req_obj.__dict__ )
        vehicle_req_obj.save()
        return HttpResponse('OK')
        
