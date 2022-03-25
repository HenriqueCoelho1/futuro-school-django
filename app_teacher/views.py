from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from app_core.models import CustomUser, Course, UserTeacher
from django.contrib.auth.decorators import login_required
from . import functions


class RegisterTeacher(View):
    def get(self, request):
        template_name = "register_teacher.html"
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        template_name = "register_teacher.html"
        context = {}
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
        if CustomUser.objects.filter(username=username).exists():
            valid_data = False
            error_param.append("username")
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
        return redirect("access")


@method_decorator(login_required, name="dispatch")
class TeacherCourses(View):
    def get(self, request):
        if not functions.validation_teacher_student(request):
            return redirect("index")
        template_name = "teacher_courses.html"
        context = {}
        current_teacher = UserTeacher.objects.get(user=request.user)
        course_list = Course.objects.all().filter(teacher=current_teacher)
        context.update({"course_list": course_list})
        return render(request, template_name, context)


@method_decorator(login_required, name="dispatch")
class RegisterTeacherCourse(View):
    def get(self, request):
        if not functions.validation_teacher_student(request):
            return redirect("index")
        template_name = "register_teacher_course.html"
        context = {}
        teacher_list = UserTeacher.objects.all()
        course_list = Course.objects.filter(teacher__isnull=True)
        context.update({"teacher_list": teacher_list, "course_list": course_list})
        return render(request, template_name, context)

    def post(self, request):
        teacher = UserTeacher.objects.get(id=request.POST.get("teacher"))
        course = Course.objects.get(id=request.POST.get("course"))
        course.teacher = teacher
        course.save()
        return redirect("teacher_courses")


@method_decorator(login_required, name="dispatch")
class RegisterCourse(View):
    def get(self, request):
        if not functions.validation_teacher_student(request):
            return redirect("index")
        template_name = "register_course.html"
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        try:
            name = request.POST.get("name")
            new_course = Course(name=name)
            new_course.save()
            return redirect("teacher_courses")
        except Exception as e:
            redirect("index")


@method_decorator(login_required, name="dispatch")
class CourseStudents(View):
    def get(self, request, id):
        if not functions.validation_teacher_student(request):
            return redirect("index")
        template_name = "course_students.html"
        context = {}
        student_list = Course.objects.get(id=id).students.all()
        course = Course.objects.get(id=id)
        context.update({"student_list": student_list, "course": course})
        return render(request, template_name, context)
