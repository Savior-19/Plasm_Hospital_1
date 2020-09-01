from django.db import models

# Create your models here.


class PatientDetails(models.Model) :
    #name = models.CharField(max_length=100, null=False, blank=False)
    age_bracket = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    status_choices = [('H', 'Hospitalized'), ('M', 'Migrated'), ('D', 'Deceased'), ('R', 'Recovered')]
    status =models.CharField(max_length=2, choices=status_choices, null=False, blank=False, default='H')
    abo_choices = [('O', 'O - Group'), ('A', 'A-Group'), ('B', 'B-Group'), ('AB', 'AB-Group')]
    blood_abo_type = models.CharField(max_length=3, choices=abo_choices, null=False, blank=False, default='AB')
    rh_choices = [('pos', 'Positive'), ('neg', 'Negative')]
    blood_rh_type = models.CharField(max_length=3, choices=rh_choices, null=False, blank=False, default='pos')

    #def __str__(self):
    #   return str(name)
