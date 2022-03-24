from django.shortcuts import render, redirect
from app_core.models import CustomUser, Course, UserTeacher, UserStudent
from django.contrib.auth.decorators import login_required
from . import functions


def register_teacher(request):
    template_name = "register_teacher.html"
    context = {}
    if request.method == "GET":
        course_list = Course.objects.all().exclude(teacher__isnull=False)
        context.update({"course_list": course_list})
        return render(request, template_name, context)
    if request.method == "POST":
        valid_data = True
        error_param = []
        formdata = {}
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        register_teacher = request.POST.get("register_teacher")
        course = request.POST.get("course")
        formdata.update(
            {
                "username": username,
                "name": name,
                "email": email,
                "register_teacher": register_teacher,
            }
        )
        if None in [username, name, email, register_teacher]:
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
        if UserTeacher.objects.filter(register=register_teacher).exists():
            valid_data = False
            error_param.append("register_teacher")
        if not functions.check_password(password):
            valid_data = False
            error_param.append("password")
        try:
            print("print-------->", course)
            if not valid_data:
                raise Exception("invalid registration data!!!")
            new_user = CustomUser(username=username, name=name, email=email)
            new_user.set_password(password)
            new_user.save()
            user_id = CustomUser.objects.get(email=email)
            course_instance = Course.objects.get(id=course)
            new_profile = UserTeacher(user=user_id, register=register_teacher)
            new_profile.save()
            course_instance.teacher = CustomUser.objects.get(email=email)
            course_instance.save()
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
    template_name = "teacher_courses.html"
    user = CustomUser.objects.get(email=request.user)
    context = {}
    if request.method == "GET":
        course_list = Course.objects.all().filter(teacher=user.id)
        context.update({"course_list": course_list})
        return render(request, template_name, context)


def teacher_students(request):
    template_name = "teacher_students.html"
    context = {}
    if request.method == "GET":
        course_list = Course.objects.get(id=2).user_student_set.all()
        context.update({"course_list": course_list})
        return render(request, template_name, context)
