from django.conf.urls import url, include
from rolety_perfect import views

app_name = "rolety_perfect"

urlpatterns = [url(r"^$", views.index, name="index"),
               url(r"^index.html/$", views.index, name="index"),
               url(r"^verticale.html/$", views.verticale, name="verticale"),
               url(r"^zaluzje.html/$", views.zaluzje, name="zaluzje"),
               url(r"^rolety-materialowe.html/$", views.rolety_materialowe, name="rolety_materialowe"),
               url(r"^rolety-zewnetrzne.html/$", views.rolety_zewnetrzne, name="rolety_zewnetrzne"),
               url(r"^moskitiery.html/$", views.moskitiery, name="moskitiery"),
               url(r"^kontakt.html/$", views.kontakt, name="kontakt")]
