from django.shortcuts import render, redirect
from Auth_App.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test


# Create your views here.


#------------------------------------------------ Teacher ------------------------------------------------------------#

@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def teacher_add(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        place = request.POST.get('place')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        image = request.FILES.get('image')

        if password == confirm_password:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('teacher-add')

            # Create the user
            user = User.objects.create_user(
                username=username, 
                password=password,
                first_name=first_name, 
                last_name=last_name,
                address=address,
                email=email,
                mobile=mobile,
                place=place,
                date_of_birth=date_of_birth,
                gender=gender,
                image=image,
                is_teacher = True
                )
            user.save()

            messages.success(request, 'Teacher Added Successfully.')
            return redirect('teacher-list')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('teacher-add')

    return render(request, 'Admin_App/teacher-add.html')
@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def teacher_list(request):
    search_query = request.GET.get('q')  # Use request.GET.get() to access query parameters
    teachers = User.objects.filter(is_teacher=True)

    # If a search query is provided, filter the teachers by the query
    if search_query:
        teachers = teachers.filter(
            Q(username__icontains=search_query) |  # Search by username
            Q(first_name__icontains=search_query) |  # Search by first name
            Q(last_name__icontains=search_query)  # Search by last name
            
        )

    context = {
        'teachers': teachers,
        'search_query': search_query,  # Pass the search query back to the template
    }

    return render(request, 'Admin_App/teacher-list.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def teacher_view(request, teacher_id):
    teacher = User.objects.get(id=teacher_id)
    context = {
        'teacher' : teacher
    }
    return render(request, 'Admin_App/teacher-view.html', context)





@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def teacher_edit(request, teacher_id):
    # Get the teacher instance to be edited
    teacher = User.objects.get(id=teacher_id)

    if request.method == 'POST':
        # Retrieve the data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        place = request.POST.get('place')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        try:
            # Check if a new image file is provided
            new_image = request.FILES.get('image')
            if new_image:
                teacher.image = new_image  # Update the teacher's image


            # Update the teacher's information
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.place = place
            teacher.address = address
            teacher.date_of_birth = date_of_birth
            teacher.gender = gender
            teacher.email = email
            teacher.mobile = mobile

            teacher.save()  # Save the updated teacher information

    
            messages.success(request, 'Teacher Updated Successfully.')
            return redirect('teacher-view', teacher_id=teacher.id)
        except:
            messages.error(request, 'Teacher Update Failed.')
            return redirect('teacher-edit')
    else:
        context = {
            'teacher': teacher
        }
        return render(request, 'Admin_App/teacher-edit.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def teacher_delete(request, teacher_id):
    teacher = User.objects.get(id=teacher_id, is_teacher=True)
    try:
        teacher.delete()
        messages.success(request, f"Teacher '{teacher.username}' Delete successfully.")
        return redirect('teacher-list')
    except:
        messages.error(request, f"Teacher '{teacher.username}' Delete Failed.")
        return redirect('teacher-list')
    

#------------------------------------------------ Student ------------------------------------------------------------#

@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')# Create your views here.
def student_add(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        place = request.POST.get('place')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        image = request.FILES.get('image')

        if password == confirm_password:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('student-add')

            # Create the user
            user = User.objects.create_user(
                username=username, 
                password=password,
                first_name=first_name, 
                last_name=last_name,
                address=address,
                email=email,
                mobile=mobile,
                place=place,
                date_of_birth=date_of_birth,
                gender=gender,
                image=image,
                is_student = True
                )
            user.save()

            messages.success(request, 'student Added Successfully.')
            return redirect('student-list')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('student-add')

    return render(request, 'Admin_App/student-add.html')


# @user_passes_test(lambda u: u.is_superuser or u.is_teacher, login_url='/Auth_App/login/')

@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def student_list(request):
    search_query = request.GET.get('q')  # Use request.GET.get() to access query parameters
    students = User.objects.filter(is_student=True)

    # If a search query is provided, filter the students by the query
    if search_query:
        students = students.filter(
            Q(username__icontains=search_query) |  # Search by username
            Q(first_name__icontains=search_query) |  # Search by first name
            Q(last_name__icontains=search_query)  # Search by last name
            
        )

    context = {
        'students': students,
        'search_query': search_query,  # Pass the search query back to the template
    }

    return render(request, 'Admin_App/student-list.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def student_view(request, student_id):
    student = User.objects.get(id=student_id)
    context = {
        'student' : student
    }
    return render(request, 'Admin_App/student-view.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def student_edit(request, student_id):
    # Get the student instance to be edited
    student = User.objects.get(id=student_id)

    if request.method == 'POST':
        # Retrieve the data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        place = request.POST.get('place')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        try:
            # Check if a new image file is provided
            new_image = request.FILES.get('image')
            if new_image:
                student.image = new_image  # Update the student's image


            # Update the student's information
            student.first_name = first_name
            student.last_name = last_name
            student.place = place
            student.address = address
            student.date_of_birth = date_of_birth
            student.gender = gender
            student.email = email
            student.mobile = mobile

            student.save()  # Save the updated student information

    
            messages.success(request, 'student Updated Successfully.')
            return redirect('student-view', student_id=student.id)
        except:
            messages.error(request, 'student Update Failed.')
            return redirect('student-edit')
    else:
        context = {
            'student': student
        }
        return render(request, 'Admin_App/student-edit.html', context)
@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')    
def student_view(request, student_id):
    student = User.objects.get(id=student_id)
    context = {
        'student' : student
    }
    return render(request, 'Admin_App/student-view.html', context)
@user_passes_test(lambda u: u.is_superuser, login_url='/Auth_App/login/')
def student_delete(request, student_id):
    student = User.objects.get(id=student_id, is_student=True)
    try:
        student.delete()
        messages.success(request, f"student '{student.username}' Delete successfully.")
        return redirect('student-list')
    except:
        messages.error(request, f"student '{student.username}' Delete Failed.")
        return redirect('student-list')
    

