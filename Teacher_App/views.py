from django.shortcuts import render, redirect
from Teacher_App.models import *
from django.contrib import messages
from django.db import transaction

# Create your views here.


def timesession_list(request):
    timesessions = TimeSession.objects.all()
    context = {
        'timesessions' : timesessions
    }
    return render(request, 'Teacher_App/timesession-list.html', context)

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
            messages.success(request, 'added successfully')
            return redirect('timesession-list')
        except Exception as e:
            messages.error(request,f'faild to add, {str(e)}')
            return redirect('timesession-add')
    return render(request, 'Teacher_App/timesection-add.html')


def timesession_edit(request, timesession_id):
    try:
        timesession = TimeSession.objects.get(id=timesession_id)
    except TimeSession.DoesNotExist:
        messages.error(request, 'Time session not found.')
        return redirect('timesession-list')

    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        try:
            # Assuming start_time and end_time are in the correct format
            timesession.start_time = start_time
            timesession.end_time = end_time
            timesession.save()
            messages.success(request, 'Edited successfully')
            return redirect('timesession-list')
        except Exception as e:
            messages.error(request, f'Failed to edit, {str(e)}')
            return redirect('timesession-edit', timesession_id=timesession.id)

    # If the request method is not POST, render the edit form
    return render(request, 'Teacher_App/timesession-edit.html', {'timesession': timesession})

def timesession_delete(request, timesession_id):
    try:
        timesession = TimeSession.objects.get(id=timesession_id)
    except TimeSession.DoesNotExist:
        messages.error(request, 'Time session not found.')
        return redirect('timesession-list')
    
    timesession.delete()


def attendance_list(request, timesession_id):
    timesession = TimeSession.objects.get(id=timesession_id)
    attendances = Attendance.objects.filter(timesession=timesession).values('date').distinct()
    context = {
        'attendances': attendances,
        'timesession': timesession,
    }
    return render(request, 'Teacher_App/attendance-list.html', context)




def attendance_delete(request, timesession_id, date):
    timesession = TimeSession.objects.get(id=timesession_id)
    
    # Filter Attendance records for the given TimeSession and the selected date
    attendance = Attendance.objects.filter(timesession=timesession, date=date)
    attendance.delete()

    return redirect('attendance-list', timesession_id=timesession.id)



    

def attendance_view(request, timesession_id, date):
    timesession = TimeSession.objects.get(id=timesession_id)
    
    # Filter Attendance records for the given TimeSession and the selected date
    attendances = Attendance.objects.filter(timesession=timesession, date=date)
    
    context = {
        'attendances': attendances,
        'timesession': timesession,
        'date': date,
    }
    
    return render(request, 'Teacher_App/attendance-view.html', context)

# def attendance_add(request, timesession_id):
#     timesession = TimeSession.objects.get(id=timesession_id)
#     user = request.user
#     attender = user
#     students = User.objects.filter(is_student=True)

#     if request.method == 'POST':
#         student_selected = request.POST.getlist('student')
#         date = request.POST.get('date')

        
#         if Attendance.objects.filter(date=date).exists():
#             messages.warning(request, f'Attendance for {date} has already been taken .')
        
#         else:
#             for student in students:
#                 if str(student.id) in student_selected:
#                     attendance = Attendance(
#                         timesession=timesession,
#                         attender=attender,
#                         student=student,
#                         attendance=True,
#                         date=date
#                     )
#                     attendance.save()
#                 else:
#                     attendance = Attendance(
#                         timesession=timesession,
#                         attender=attender,
#                         student=student,
#                         attendance=False,
#                         date=date
#                     )
#                     attendance.save()
            
#             messages.success(request, 'added successfully')
#             return redirect('attendance-list')
    
#     return render(request, 'attendance-add.html')



def attendance_add(request, timesession_id):
    timesession = TimeSession.objects.get(id=timesession_id)
    user = request.user
    attender = user

    students = User.objects.filter(is_student=True)  # Moved this line outside of the if block

    if request.method == 'POST':
        student_selected = request.POST.getlist('student')
        date = request.POST.get('date')

        # Add validation for date and student_selected
        if not date or not student_selected:
            # Handle validation error here
            messages.error(request, 'Invalid input data')
            return redirect('attendance-add')  # Redirect to the add form
        
        if Attendance.objects.filter(date=date).exists():
            messages.error(request, f'Attendance for {date} has already been taken .')


        # Use a database transaction to ensure atomicity
        with transaction.atomic():
            if Attendance.objects.filter(date=date).exists():
                messages.warning(request, f'Attendance for {date} has already been taken.')
                return redirect('attendance-add', timesession_id=timesession_id)
            else:
                for student in students:
                    attendance = Attendance(
                        timesession=timesession,
                        attender=attender,
                        student=student,
                        attendance=str(student.id) in student_selected,
                        date=date
                    )
                    attendance.save()

            messages.success(request, 'Added successfully')
            return redirect('attendance-list', timesession_id=timesession_id)

    
    context = {
        'students': students  # Use the 'students' variable in the context
    }
    
    return render(request, 'Teacher_App/attendance-add.html', context)






def attendance_edit(request, timesession_id, date):
    timesession = TimeSession.objects.get(id=timesession_id)
    user = request.user
    attender = user

    students = User.objects.filter(is_student=True)

    # Get the attendance records for the given time session and date
    attendance_records = Attendance.objects.filter(
        timesession=timesession,
        date=date
    )

    if request.method == 'POST':
        student_selected = request.POST.getlist('student')

        # Add validation for student_selected
        if not student_selected:
            messages.error(request, 'Invalid input data')
            return redirect('attendance-edit', timesession_id=timesession_id, date=date)

        # Use a database transaction to ensure atomicity
        with transaction.atomic():
            for student in students:
                attendance, created = Attendance.objects.get_or_create(
                    timesession=timesession,
                    attender=attender,
                    student=student,
                    date=date
                )
                # Update the attendance status based on the selected students
                attendance.attendance = str(student.id) in student_selected
                attendance.save()

            messages.success(request, 'Updated successfully')
            return redirect('attendance-list', timesession_id=timesession_id)

    context = {
        'students': students,
        'attendance_records': attendance_records,
        'date': date,
    }

    return render(request, 'Teacher_App/attendance-edit.html', context)



def studymaterial_list(request):
    user = request.user  # Get the user from the request

    if user.is_superuser:
        studymaterials = StudyMaterial.objects.all()
    else:
        studymaterials = StudyMaterial.objects.filter(user=user)

    context = {
        'studymaterials': studymaterials
    }
    return render(request, 'Teacher_App/studymaterial-list.html', context)


def studymaterial_view(request, studymaterial_id):
    studymaterial = StudyMaterial.objects.get(id=studymaterial_id)
    context = {
        'studymaterial' : studymaterial
    }
    return render(request, 'Teacher_App/studymaterial-view.html', context)

def studymaterial_add(request):
    user = request.user
    if request.method == 'POST':
        text = request.POST.get('text') or None
        image = request.FILES.get('image') or None

        studymaterial = StudyMaterial(
            text=text,
            image=image,
            user=user
        )
        studymaterial.save()
        messages.success(request, 'Added Successfully')
        return redirect('studymaterial-list')
    return render(request, 'Teacher_App/studymaterial-add.html')

def studymaterial_edit(request, studymaterial_id):
    studymaterial = StudyMaterial.objects.get(id=studymaterial_id)
    user = request.user
    if request.method == 'POST':
        text = request.POST.get('text')
        image = request.FILES.get('image')

        try:
            studymaterial.text=text
            studymaterial.image=image
            studymaterial.user=user
            studymaterial.save()
            messages.success(request, 'Added successfully')
            return redirect('studymaterial-list')
        
        except Exception as e:
            messages.error(request, f'faild to add {str(e)}')
            return redirect('studymaterial-edit', studymaterial_id=studymaterial.id)
    return render(request, 'Teacher_App/studymaterial-edit.html')

def studymaterial_delete(request, studymaterial_id):
    studymaterial = StudyMaterial.objects.get(id=studymaterial_id)
    studymaterial.delete()
    return redirect('studymaterial-delete')

