from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from rest_framework import generics
from .models import PatientDetails
from .serializers import PatientDetailsSerializer
import io
import csv

# Create your views here.

class PatientDetailsListView(generics.ListAPIView) :
    #lookup_field = 'blood_abo_type'
    serializer_class = PatientDetailsSerializer

    def get_queryset(self):
        MAX_PATIENT_COUNT_THRESHOLD = 100
        MIN_PATIENT_COUNT_THRESHOLD = 10

        abo_type = self.kwargs.get("abo")
        rh_type = self.kwargs.get("rh")
        cur_city = self.kwargs.get("city")
        cur_district = self.kwargs.get("district")
        cur_state = self.kwargs.get("state")
        
        patient_list = PatientDetails.objects.filter(status='R', blood_abo_type=abo_type, blood_rh_type=rh_type)
        
        if cur_state != "" and len(patient_list) > MAX_PATIENT_COUNT_THRESHOLD :
            modified_list = patient_list.filter(state=cur_state)
            if len(modified_list) > MIN_PATIENT_COUNT_THRESHOLD :
                patient_list = modified_list

        if cur_district != "" and len(patient_list) > MAX_PATIENT_COUNT_THRESHOLD :
            modified_list = patient_list.filter(district=cur_district)
            if len(modified_list) > MIN_PATIENT_COUNT_THRESHOLD :
                patient_list = modified_list

        if cur_city != "" and len(patient_list) > MAX_PATIENT_COUNT_THRESHOLD :
            patient_list = patient_list.filter(city=cur_city)
            if len(modified_list) > MIN_PATIENT_COUNT_THRESHOLD :
                patient_list = modified_list
        
        return patient_list

    """def get_object(self):
        abo_type = self.kwargs.get("abo")
        rh_type = self.kwargs.get("rh")
        state = self.kwargs.get("state")
        status = 'R'
        #return PatientDetails.objects.filter(blood_abo_type=abo_type, blood_rh_type=rh_type)
        return PatientDetails.objects.all()"""
