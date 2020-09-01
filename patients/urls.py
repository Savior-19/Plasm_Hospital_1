from django.urls import path

from .views import PatientDetailsListView

urlpatterns = [
    #path('abo=<str:abo>?rh=<str:rh>?state=<str:state>?', PatientDetailsListView.as_view(), name='patient_list'),
    path('abo="<str:abo>"/rh="<str:rh>"', PatientDetailsListView.as_view())
]