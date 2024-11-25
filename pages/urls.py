from django.urls import path

from pages import views

urlpatterns = [
    path("", views.home_uz, name="home"),
    path("uz", views.home_uz, name="home_uz"),
    path("ru", views.home_ru, name="home_ru"),
    path("en", views.home_en, name="home_en"),
]