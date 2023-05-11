from django.contrib import admin
from .models import Hospitals, Doctors, Categories, Contact

# Register your models here.


class HospitalsAdmin(admin.ModelAdmin):
    search_fields = [
        "nomi",
        "tuman",
    ]
    list_filter = ["ish_vaqti", "created_at"]


class DoctorsAdmin(admin.ModelAdmin):
    search_fields = ["ismi", "familiya"]
    list_filter = ["ish_vaqti", "created_at", "korik_narxi"]


class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ["nomi"]


admin.site.register(Hospitals, HospitalsAdmin)
admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Categories, CategoriesAdmin)
