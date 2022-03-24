from django.shortcuts import render, redirect
from app_core.models import CustomUser, Course, UserTeacher, UserStudent
from django.contrib.auth.decorators import login_required
from . import functions


def register_teacher(request):
    template_name = "register_teacher.html"
    context = {}
    if request.method == "GET":
        return render(request, template_name, context)
    if request.method == "POST":
        valid_data = True
        error_param = []
        formdata = {}
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        id_teacher = request.POST.get("id_teacher")
        formdata.update(
            {
                "username": username,
                "name": name,
                "email": email,
                "id_teacher": id_teacher,
            }
        )
        if None in [username, name, email, id_teacher]:
            valid_data = False
        if CustomUser.objects.filter(email=email).exists() or not functions.check_email(
            email
        ):
            valid_data = False
            error_param.append("email")
        # if not functions.check_username(username):
        #     valid_data = False
        #     error_param.append("username")
        if not functions.check_name(name):
            valid_data = False
            error_param.append("name")
        if UserTeacher.objects.filter(register=id_teacher).exists():
            valid_data = False
            error_param.append("id_teacher")
        if not functions.check_password(password):
            valid_data = False
            error_param.append("password")
        try:
            if not valid_data:
                raise Exception("invalid registration data!!!")
            new_user = CustomUser(username=username, name=name, email=email)
            new_user.set_password(password)
            new_user.save()
            user_id = CustomUser.objects.get(email=email)
            new_profile = UserTeacher(user=user_id, register=id_teacher)
            new_profile.save()
        except Exception as e:
            print(e)
            valid_data = False
        if not valid_data:
            return render(
                request,
                template_name,
                {"ok": False, "errors": error_param, "formdata": formdata},
            )
        return redirect("register_student")


@login_required
def teacher_courses(request):
    if not functions.validation_teacher_student(request):
        return redirect("index")
    template_name = "teacher_courses.html"
    user = CustomUser.objects.get(email=request.user)
    context = {}
    if request.method == "GET":
        print("---> print", request.user)
        current_teacher = UserTeacher.objects.get(user=request.user)
        course_list = Course.objects.all().filter(teacher=current_teacher)
        context.update({"course_list": course_list})
        return render(request, template_name, context)


@login_required
def register_teacher_course(request):
    if not functions.validation_teacher_student(request):
        return redirect("index")
    template_name = "register_teacher_course.html"
    context = {}
    if request.method == "GET":
        teacher_list = UserTeacher.objects.all()
        course_list = Course.objects.filter(teacher__isnull=True)
        context.update({"teacher_list": teacher_list, "course_list": course_list})
        return render(request, template_name, context)
    elif request.method == "POST":
        teacher = UserTeacher.objects.get(id=request.POST.get("teacher"))
        print("---> print", teacher)
        course = Course.objects.get(id=request.POST.get("course"))
        course.teacher = teacher
        course.save()
    return redirect("teacher_courses")


@login_required
def register_course(request):
    if not functions.validation_teacher_student(request):
        return redirect("index")
    template_name = "register_course.html"
    context = {}
    if request.method == "GET":
        return render(request, template_name, context)

    if request.method == "POST":
        try:
            name = request.POST.get("name")
            new_course = Course(name=name)
            new_course.save()
        except Exception as e:
            redirect("index")
    return redirect("teacher_courses")


@login_required
def course_students(request, id):
    if not functions.validation_teacher_student(request):
        return redirect("index")
    template_name = "course_students.html"
    context = {}
    if request.method == "GET":
        student_list = Course.objects.get(id=id).students.all()
        course = Course.objects.get(id=id)
        context.update({"student_list": student_list, "course": course})
        return render(request, template_name, context)
