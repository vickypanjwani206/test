from django.shortcuts import render,redirect
from restaurant.forms import *
from django.contrib import messages


def showMain(request):
    return render(request,"restaurant/main.html")


def registerPage(request):
    return render(request,"restaurant/register.html",{"rf":RestaurantForm()})


def save_res(request):
    rf = RestaurantForm(request.POST)
    if rf.is_valid():
        db = rf.save(commit=False)
        db.restro_otp = 4321
        db.restro_status = 'pending'
        db.save()
        messages.success(request,"After approval you will get the message")
        return redirect('restro')
    else:
        return render(request,"restaurant/register.html",{"rf":rf})