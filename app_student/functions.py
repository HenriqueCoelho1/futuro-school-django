import re


def validation_teacher_student(request):
    try:
        print(request.user.student)
        return True
    except:
        return False


def check_name(name) -> bool:
    regex = r"^[a-zA-Z]+$"
    if re.fullmatch(regex, name):
        return True
    else:
        return False


def check_email(email) -> bool:
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def check_cpf(cpf) -> bool:
    regex = r"[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}"
    if re.fullmatch(regex, cpf):
        return True
    else:
        return False


def check_password(password) -> bool:
    reg = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    if re.search(re.compile(reg), password):
        return True
    else:
        return False


def check_username(username) -> bool:
    reg = "^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$"
    if re.search(re.compile(reg), username):
        return True
    else:
        return False
