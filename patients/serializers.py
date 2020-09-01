from rest_framework import serializers

from .models import PatientDetails

class PatientDetailsSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PatientDetails
        fields = [
            #'name',
            'age_bracket',
            'gender',
            'city',
            'district',
            'state',
            'nationality',
            'status',
            'blood_abo_type',
            'blood_rh_type'
        ]