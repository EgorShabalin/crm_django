from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, EditUserForm
from .models import *
from custom_user.models import User


def index(request):
    return render(
        request,
        "site_app/index.html",
        {},
    )


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/")

    else:
        form = SignupForm()

    return render(request, "site_app/signup.html", {"form": form})


@login_required
def profile(request, pk):
    profile = User.objects.get(id=pk)

    return render(
        request,
        "site_app/profile.html",
        {
            "profile": profile,
        },
    )


@login_required
def edit_profile(request):
    current_user = User.objects.get(id=request.user.id)
    if request.user.is_authenticated:
        form = EditUserForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect("site_app:login")

        return render(request, "site_app/edit_profile.html", {"form": form})


@login_required
def table(request):
    students = Student.objects.all()
    field_names = []
    for field in Student._meta.fields:
        field_names.append(field.verbose_name)
    student_values = []
    for student in students:
        values = [
            (field.name, getattr(student, field.name)) for field in Student._meta.fields
        ]
        student_values.append(dict(values))
    return render(
        request,
        "site_app/table.html",
        {
            "students": students,
            "field_names": field_names,
            "student_values": student_values,
        },
    )


@login_required
def grid(request):
    students = Student.objects.all()
    field_names = []
    for field in Student._meta.fields:
        field_names.append(field.verbose_name)
    student_values = []
    for student in students:
        values = [
            (field.name, getattr(student, field.name)) for field in Student._meta.fields
        ]
        student_values.append(dict(values))
    return render(
        request,
        "site_app/grid.html",
        {
            "students": students,
            "field_names": field_names,
            "student_values": student_values,
        },
    )


def create_grid_content(cls, queryset):
    columns = []
    for field in cls._meta.fields:
        columns.append(field.verbose_name)
    dicts_list = []
    for i in queryset:
        key_value_pairs = [
            (field.verbose_name, getattr(i, field.name)) for field in cls._meta.fields
        ]
        dicts_list.append(dict(key_value_pairs))
    result = [columns, dicts_list]
    return result


@login_required
def tabulator(request):
    students = Student.objects.all()
    content = create_grid_content(Student, students)
    field_names = content[0]
    student_values = content[1]
    # field_names = []
    # for field in Student._meta.fields:
    #    field_names.append(field.name)
    # student_values = []
    # for student in students:
    #    values = [
    #        (field.name, getattr(student, field.name)) for field in Student._meta.fields
    #    ]
    #    student_values.append(dict(values))
    return render(
        request,
        "site_app/tabulator.html",
        {
            "students": students,
            "field_names": field_names,
            "student_values": student_values,
        },
    )


@login_required
def ag_grid(request):
    students = Student.objects.all()
    content = create_grid_content(Student, students)
    column_names = content[0]
    student_dict_list = content[1]

    return render(
        request,
        "site_app/ag_grid.html",
        {
            "students": students,
            "column_names": column_names,
            "student_dict_list": student_dict_list,
        },
    )


@login_required
def student(request, pk):
    current_student = Student.objects.get(id=pk)
    representatives = Representative.objects.filter(student=current_student)
    courses = Course.objects.filter(student=current_student)
    grades = Grade.objects.filter(student=current_student)

    representatives_content = create_grid_content(Representative, representatives)
    representatives_columns = representatives_content[0]
    representative_dicts_list = representatives_content[1]

    grades_content = create_grid_content(Grade, grades)
    grades_columns = grades_content[0]
    grades_dicts_list = grades_content[1]

    courses_content = create_grid_content(Course, courses)
    courses_columns = courses_content[0]
    courses_dicts_list = courses_content[1]

    return render(
        request,
        "site_app/student.html",
        {
            "current_student": current_student,
            "representatives": representatives,
            "representatives_columns": representatives_columns,
            "representative_dicts_list": representative_dicts_list,
            "grades_columns": grades_columns,
            "grades_dicts_list": grades_dicts_list,
            "courses": courses,
            "courses_columns": courses_columns,
            "courses_dicts_list": courses_dicts_list,
        },
    )
