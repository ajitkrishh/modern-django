from django.urls import path

from .views import *

urlpatterns = [
    path('profile/<int:pk>/edit', update_profile,name = "update"),
    path('profile/edit', update_profile,name = "update"),
    path('register/', registration,name = "register"),
    # path('vehicles/', get_vehicle,name = "vehicles"),
    # path('vehicles-status/', activate_deacticate_vehicle,name = "activate_deacticate_vehicle"),
    # path('vehicles-request/', vehicle_connection_request,name = "vehicle_connection_request"),
    # path('add-vehicle/', add_vehicle,name = "add_vehicle"),
    
    
    
] 

