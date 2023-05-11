from django.shortcuts import render
from hospital.models import Contact


def landing_page(request):
    if request.method == "GET":
        return render(request, "index.html")
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
