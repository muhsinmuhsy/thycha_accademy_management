from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Core_App.models import *
from django.contrib import messages

# Create your views here.

@login_required(login_url='Auth_App/login')
def dashboard(request):
    return render (request, 'Core_App/dashboard.html')

def notification_list(request):
    notifications = Notification.objects.all().order_by('-id')
    context = {
        'notifications' : notifications
    }
    return render(request, 'Core_App/notification-list.html', context)

def notification_add(request):
    user = request.user
    if request.method == 'POST':
        text = request.POST.get('text')
        try:
            notification = Notification(
                user=user,
                text=text
            )
            notification.save()
            messages.success(request, 'notfication added successfully')
            return redirect('notification-list')
        except Exception as e:
            messages.error(request, f'Error adding notification: {str(e)}')
            return redirect('notification-add')
    return render(request, 'Core_App/notification-add.html')


def notification_edit(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    if request.method == 'POST':
        notification.text = request.POST.get('text')
        try:
            notification.save()
            messages.success(request, 'Notification updated successfully')
            return redirect('notification-list')
        except Exception as e:
            messages.error(request, f'Error updating: {str(e)}')
            return redirect('notification-edit', notification_id=notification.id)
    return render(request, 'Core_App/notification-edit.html')

def notification_delete(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    try:
        notification.delete()
        messages.success(request, 'Notification delete successfully')
        return redirect('notification-list')
    except Exception as e:
        messages.error(request, f'Notification delete failed: {str(e)}')
        return redirect('notification-list')

