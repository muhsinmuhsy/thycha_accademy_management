from django.urls import path
from Core_App.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('notification/list', notification_list, name='notification-list'),
    path('notification/add', notification_add, name='notification-add'),
    path('notification/<int:notification_id>/edit', notification_edit, name='notification-edit'),
    path('notification/<int:notification_id>/delete', notification_delete, name='notification-delete')
]