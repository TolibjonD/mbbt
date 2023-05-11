from django.urls import path
from .views import (
    hospitals,
    doctors,
    contact,
    hospital_detail_page,
    doctors_detail_page,
)

app_name = "hospital"
urlpatterns = [
    path("hospitals/", hospitals, name="hospitals"),
    path("doctors/", doctors, name="doctors"),
    path("contact/", contact, name="contact"),
    path("detail/<int:id>/", hospital_detail_page, name="detail"),
    path("detail-doctor/<int:id>/", doctors_detail_page, name="detail-d"),
]
