from django.shortcuts import render
from .models import Hospitals, Doctors, Contact
from django.shortcuts import redirect

# Create your views here.


def hospitals(request):
    if request.method == "GET":
        hospitals = Hospitals.objects.all().order_by("-created_at")
        count = Hospitals.objects.all().count()
        context = {
            "hospitals": hospitals,
            "count": count,
        }
        return render(request, "hospitals.html", context=context)


def doctors(request):
    if request.method == "GET":
        doctors = Doctors.objects.all().order_by("-created_at")
        context = {
            "doctors": doctors,
        }
        return render(request, "doctors.html", context=context)


def contact(request):
    if request.method == "GET":
        return render(request, "contact.html")

    else:
        name = request.POST["name"]
        tel = request.POST["tel"]
        msg = request.POST["message"]
        if name and tel and msg:
            Contact.objects.create(ismi=name, telefon=tel, message=msg)
            success = "Muvaffaqiyatli yuborildi. "
            return render(request, "contact.html", {"success": success})
        else:
            error = "Qaysidur maydon to'ldirilmagan . Iltimos barcha maydonlarni to'ldiring."
            return render(request, "contact.html", {"error": error})


def hospital_detail_page(request, id):
    hospital = Hospitals.objects.get(id=id)
    return render(request, "hospital_detail.html", {"hospital": hospital})


def doctors_detail_page(request, id):
    doctor = Doctors.objects.get(id=id)
    return render(request, "doctor_detail.html", {"doctor": doctor})
