from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from app_core.models import CustomUser, Course, UserStudent
from . import functions
from django.contrib.auth.decorators import login_required
from validate_docbr import CPF

cpf_validate = CPF()


class RegisterStudent(View):
    def get(self, request):
        template_name = "register_student.html"
        context = {}
        course_list = Course.objects.all().exclude(teacher__isnull=True)
        context.update({"course_list": course_list})
        return render(request, template_name, context)

    def post(self, request):
        template_name = "register_student.html"
        context = {}
        valid_data = True
        error_param = []
        formdata = {}
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpf = request.POST.get("cpf")
        course = request.POST.get("course")
        formdata.update(
            {
                "username": username,
                "name": name,
                "email": email,
                "cpf": cpf,
            }
        )

        if None in [username, name, email, cpf]:
            valid_data = False
        if CustomUser.objects.filter(email=email).exists() or not functions.check_email(
            email
        ):
            valid_data = False
            error_param.append("email")
        if CustomUser.objects.filter(username=username).exists():
            valid_data = False
            error_param.append("username")
        if not functions.check_name(name):
            valid_data = False
            error_param.append("name")
        if UserStudent.objects.filter(cpf=cpf).exists() or not cpf_validate.validate(
            cpf
        ):
            valid_data = False
            error_param.append("cpf")
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
            new_profile = UserStudent(user=user_id, cpf=cpf)
            new_profile.save()
            user_id2 = UserStudent.objects.get(cpf=cpf)
            for course_id in course:
                user_id2.courses.add(Course.objects.get(id=course_id))
        except Exception as e:
            valid_data = False
        if not valid_data:
            return render(
                request,
                template_name,
                {"ok": False, "errors": error_param, "formdata": formdata},
            )
        return redirect("register_student")


@method_decorator(login_required, name="dispatch")
class StudentCourses(View):
    def get(self, request):
        if not functions.validation_teacher_student(request):
            return redirect("index")
        template_name = "student_courses.html"
        context = {}
        course_list = UserStudent.objects.get(user=request.user.id).courses.all()
        context.update({"course_list": course_list})
        return render(request, template_name, context)
