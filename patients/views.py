from django.shortcuts import render

from rest_framework import generics
from .models import PatientDetails
from .serializers import PatientDetailsSerializer

# Create your views here.

class PatientDetailsListView(generics.ListAPIView) :
    #lookup_field = 'blood_abo_type'
    serializer_class = PatientDetailsSerializer

    def get_queryset(self):
        abo_type = self.kwargs.get("abo")
        rh_type = self.kwargs.get("rh")
        return PatientDetails.objects.filter(blood_abo_type=abo_type)

    """def get_object(self):
        abo_type = self.kwargs.get("abo")
        rh_type = self.kwargs.get("rh")
        state = self.kwargs.get("state")
        status = 'R'
        #return PatientDetails.objects.filter(blood_abo_type=abo_type, blood_rh_type=rh_type)
        return PatientDetails.objects.all()"""