from django.urls import path
from  Admin_App.views import *

urlpatterns = [
    path('teacher/add/', teacher_add, name='teacher-add'),
    path('teacher/list/', teacher_list, name='teacher-list'),
    path('teacher/<int:teacher_id>/view', teacher_view, name='teacher-view'),
    path('teacher/<int:teacher_id>/edit', teacher_edit, name='teacher-edit'),
    path('teacher/<int:teacher_id>/delete', teacher_delete, name='teacher-delete'),

    path('student/add/', student_add, name='student-add'),
    path('student/list/', student_list, name='student-list'),
    path('student/<int:student_id>/view', student_view, name='student-view'),
    path('student/<int:student_id>/edit', student_edit, name='student-edit'),
    path('student/<int:student_id>/delete', student_delete, name='student-delete'),

]