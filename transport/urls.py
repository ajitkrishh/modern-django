from django.urls import path

from .views import company_action

urlpatterns = [
    path("a/", company_action, name="company-action"),
    # path('vehicles/', get_vehicle,name = "vehicles"),
    # path('vehicles-status/', activate_deacticate_vehicle,name = "activate_deacticate_vehicle"),
    # path('vehicles-request/', vehicle_connection_request,name = "vehicle_connection_request"),
    # path('add-vehicle/', add_vehicle,name = "add_vehicle"),
]
