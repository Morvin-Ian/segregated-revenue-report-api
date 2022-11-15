from django.urls import path
from .views import *


urlpatterns = [

    # Revenue
    path('revenue/', RevenueList.as_view()),
    path('revenue/<int:pk>/', RevenueDetail.as_view()),

    path('revenue/department/registration/', RegistrationTotal.as_view()),
    path('revenue/department/laboratory/', LaboratoryTotal.as_view()),
    path('revenue/department/pharmacy/', PharmacyTotal.as_view()),
    path('revenue/department/radiology/', RadiologyTotal.as_view()),
    path('revenue/department/procedure/', ProceduresTotal.as_view()),

    path('revenue/payment/<str:method>/', PaymentMethodCount.as_view()),

    
]

