from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Appointment
from ..loginreg.models import User
from django.contrib import messages
from datetime import datetime, date
from django.db.models import Q
now = datetime.now()

def index(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    user = User.objects.get(id=request.session["id"])
    context = {
        "today": Appointment.objects.filter(Q(start_date__lte=now, start_date__gte=now) & Q(creator__full_name=request.session["full_name"])),
        "future": Appointment.objects.filter(creator__full_name=request.session["full_name"]).exclude(start_date__lte=now)
    }
    return render(request, 'pythonbelt2app/index.html', context)

def edit(request, appointment_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    context = {
        "appointment": Appointment.objects.get(id=appointment_id),
        "users": User.objects.all()
    }
    return render(request, 'pythonbelt2app/edit.html', context)

def create(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    if request.POST["start_date"] and request.POST["start_time"] and request.POST["task"]:
        user = User.objects.get(id=request.session['id'])
        task = request.POST["task"]
        start_date = datetime.strptime(request.POST["start_date"], '%Y-%m-%d')
        start_time = datetime.strptime(request.POST["start_time"], '%H:%M')
        # if not start_date < now:
        if start_date:
            appointment = Appointment.objects.create(task=task, start_date=start_date, start_time=start_time, creator=user)
            return redirect(reverse('pythonbelt2app:index'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Try again')
            return redirect(reverse('pythonbelt2app:index'))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        return redirect(reverse('pythonbelt2app:index'))

def update(request, appointment_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    if request.POST["start_date"] and request.POST["start_time"] and request.POST["task"] and request.POST["status"]:
        a = Appointment.objects.get(id=appointment_id)
        a.task = request.POST["task"]
        a.status = request.POST["status"]
        a.start_date = datetime.strptime(request.POST["start_date"], '%Y-%m-%d')
        a.start_time = datetime.strptime(request.POST["start_time"], '%H:%M')
        # if not a.start_date < now:
        if start_date:
            a.save()
        else:
            messages.add_message(request, messages.SUCCESS, 'Try again')
            a = Appointment.objects.get(id=appointment_id)
            return redirect(reverse('pythonbelt2app:edit', kwargs={"appointment_id":a.id}))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        a = Appointment.objects.get(id=appointment_id)
        return redirect(reverse('pythonbelt2app:edit', kwargs={"appointment_id":a.id}))
    return redirect(reverse('pythonbelt2app:index'))

def delete(request, appointment_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    context = {
        "appointment": Appointment.objects.get(id=appointment_id),
        "users": User.objects.all()
    }
    return render(request, 'pythonbelt2app/delete.html', context)

def destroy(request, appointment_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect(reverse('pythonbelt2app:index'))
