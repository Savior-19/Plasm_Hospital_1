from django.urls import path

from .views import PatientDetailsListView

urlpatterns = [
    path('abo=<str:abo>&rh=<str:rh>&city=<str:city>&district=<str:district>&state=<str:state>/', PatientDetailsListView.as_view()),
]
