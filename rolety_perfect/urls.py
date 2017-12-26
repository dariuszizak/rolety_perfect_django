from django.conf.urls import url, include
from rolety_perfect import views

app_name = "rolety_perfect"

urlpatterns = [url(r"^$", views.page, name="index"),
               url(r"^index.html/$", views.page, name="index"),
               url(r"^verticale.html/$", views.page, name="verticale"),
               url(r"^zaluzje.html/$", views.page, name="zaluzje"),
               url(r"^rolety-materialowe.html/$", views.page, name="rolety_materialowe"),
               url(r"^rolety-zewnetrzne.html/$", views.page, name="rolety_zewnetrzne"),
               url(r"^moskitiery.html/$", views.page, name="moskitiery"),
               url(r"^kontakt.html/$", views.page, name="kontakt")]
