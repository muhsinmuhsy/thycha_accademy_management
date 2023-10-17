from django.shortcuts import render, redirect
from Teacher_App.models import *
from django.contrib import messages

# Create your views here.

def timesession_add(request):
    if request.method=='POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        try:

            timesession = TimeSession(
                start_time = start_time,
                end_time = end_time
            )
            timesession.save()
            messages.success('added successfully')
            return redirect('timesession-list')
        except Exception as e:
            messages.error(request,f'faild to add, {str(e)}')
            return redirect('timesession-add')
    return render(request, 'Teacher_App/add-timesection.html')

def timesession_list(request):
    timesession = TimeSession.objects.all()
    context = {
        'timesession' : timesession
    }
    return render(request, 'Teacher_App/timesession-list', context)
