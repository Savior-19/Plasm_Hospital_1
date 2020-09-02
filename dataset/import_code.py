# Run `python manage.py shell` and then run the following code.

import csv
import os

from patients.models import PatientDetails

path = "/Users/aadhitya/Documents/GitHub/Plasm_Hospital_1/dataset"
os.chdir(path)

with open('data1.csv') as csvfile :
    reader = csv.DictReader(csvfile)
    for row in reader :
        status_inp = row["Current Status"]
        if status_inp=="Hospitalized" :
            status = 'H'
        elif status_inp=="Recovered" :
            status = 'R'
        elif status_inp=="Deceased" :
            status = 'D'
        elif status_inp=="Migrated" :
            status = 'M'
        obj = PatientDetails(
            age_bracket = row["Age Bracket"],
            gender = row["Gender"],
            city = row["Detected City"],
            district = row["Detected District"],
            state = row["Detected State"],
            nationality = row["Nationality"],
            status = status,
            blood_abo_type = row["ABO"],
            blood_rh_type = row["Rh"]
        )
        obj.save()
