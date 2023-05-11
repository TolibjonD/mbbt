from django.db import models
from django.utils import timezone


# Create your models here.
class Hospitals(models.Model):
    class Tumanlar(models.TextChoices):
        Chortoq_tumani = "Chortoq tumani"
        Chust_tumani = "Chust tumani"
        Kosonsoy_tumani = "Kosonsoy tumani"
        Mingbuloq_tumani = "Mingbuloq tumani"
        Namangan_tumani = "Namangan tumani"
        Norin_tumani = "Norin tumani"
        Pop_tumani = "Pop tumani"
        turaqurgon_tumani = "To'raqo'rg'on tumani"
        uchkurgan_tumani = "Uchqo'rg'on tumani"
        Uychi_tumani = "Uychi tumani"
        Yangikurgan_tumani = "Yangiqo'rg'on tumani"
        Davlatobod_tumani = "Davlatobod tumani"
        yangi_namangan = "Yangi Namangan tumani"
        namangan_shaxri = "Namangan shahri"

    class Yotoq(models.TextChoices):
        mavjud = "Mavjud"
        mavjud_emas = "Mavjud emas"

    nomi = models.CharField(max_length=300)
    tuman = models.TextField(
        max_length=100, choices=Tumanlar.choices, default="Namangan shahri"
    )
    ishchilar_soni = models.PositiveIntegerField()
    telefon = models.CharField(max_length=30)
    yotoq_joyi = models.CharField(
        max_length=100, choices=Yotoq.choices, default="mavjud"
    )
    ish_vaqti = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="hospitals/", default="contact.jpg")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tuman: {self.tuman} . Nomi: {self.nomi}"


class Categories(models.Model):
    nomi = models.CharField(max_length=250)
    shifoxona = models.ForeignKey(
        Hospitals, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return self.nomi


class Doctors(models.Model):
    shifoxona = models.ForeignKey(
        Hospitals, on_delete=models.CASCADE, related_name="doctors"
    )
    bolim = models.ForeignKey(Categories, on_delete=models.CASCADE)
    ismi = models.CharField(max_length=120)
    familiya = models.CharField(max_length=120)
    telefon = models.CharField(max_length=30)
    korik_narxi = models.DecimalField(max_digits=16, decimal_places=2)
    photo = models.ImageField(upload_to="doctors/", default="doctor.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    ish_vaqti = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return f"Ismi: {self.ismi} . Familiya: {self.familiya} . Ish joyi: {self.shifoxona.nomi}"

    def get_full_name(self):
        return f"{self.ismi} {self.familiya}"


class Contact(models.Model):
    ismi = models.CharField(max_length=120)
    telefon = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ismi
