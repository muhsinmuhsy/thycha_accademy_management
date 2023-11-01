from django.urls import path
from Teacher_App.views import *

urlpatterns = [
    path('timesession/list', timesession_list, name='timesession-list'),
    path('timesession/add', timesession_add, name='timesession-add'),
    path('timesession/<int:timesession_id>/edit', timesession_edit, name='timesession-edit'),
    path('timesession/<int:timesession_id>/delete', timesession_delete, name='timesession-delete'),

    path('attendance/<int:timesession_id>/list/', attendance_list, name='attendance-list'),
    path('attendance/<int:timesession_id>/view/<str:date>/', attendance_view, name='attendance-view'),
    path('attendance/<int:timesession_id>/add/', attendance_add, name='attendance-add'),
    path('attendance/<int:timesession_id>/<str:date>/delete/', attendance_delete, name='attendance-delete'),
    path('attendance/edit/<int:timesession_id>/<str:date>/', attendance_edit, name='attendance-edit'),


    path('studymaterial/list/', studymaterial_list, name='studymaterial-list'),
    path('studymaterial/<int:studymaterial_id>/view/', studymaterial_view, name='studymaterial-view'),
    path('studymaterial/add/', studymaterial_add, name='studymaterial-add'),
    path('studymaterial/<int:studymaterial_id>/delete/', studymaterial_delete, name='studymaterial-delete'),
    path('studymaterial/<int:studymaterial_id>/edit/', studymaterial_edit, name='studymaterial-edit'),
    
]