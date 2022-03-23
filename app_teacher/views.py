from django.shortcuts import render, redirect
from app_core.models import CustomUser, UserType, Course
from . import functions


def register_teacher(request):
    template_name = "register_teacher.html"
    context = {}
    if request.method == "GET":
        course_list = Course.objects.all()
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
        ### essa tive que tirar essa verificação porque dá invalid registration data

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
        if UserType.objects.filter(
            identifier=register_teacher
        ).exists() or not functions.check_username(username):
            valid_data = False
            error_param.append("register_teacher")
        if not functions.check_password(password):
            valid_data = False
            error_param.append("password")
        try:
            print(course)
            if not valid_data:
                raise Exception("invalid registration data!!!")
            course_id = Course.objects.get(id=course)
            new_user = CustomUser(
                username=username, name=name, email=email, course=course_id
            )
            new_user.set_password(password)
            new_user.save()
            user_id = CustomUser.objects.get(email=email)
            new_profile = UserType(
                user=user_id, identifier=register_teacher, user_type="T"
            )

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
