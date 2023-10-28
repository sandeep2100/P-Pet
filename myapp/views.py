from django.shortcuts import render, redirect
from .models import *
from datetime import datetime, timedelta


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        pet = request.POST.get("pet")
        date = request.POST.get("date")
        time = request.POST.get("time")
        selected_service = request.POST.get("selected_service")

        en = Appointment(
            name=name,
            email=email,
            number=number,
            pet=pet,
            date=date,
            time=time,
            selected_service=selected_service
        )
        en.save()
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def price(request):
    return render(request, "price.html")


def service(request):
    return render(request, "service.html")


def team(request):
    return render(request, "team.html")


def testimonial(request):
    return render(request, "testimonial.html")


def booking(request):
    return render(request, "booking.html")


def contact(request):
    return render(request, "contact.html")
