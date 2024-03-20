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


@login_required
def tabulator(request):
    students = Student.objects.all()
    field_names = []
    for field in Student._meta.fields:
        field_names.append(field.name)
    student_values = []
    for student in students:
        values = [
            (field.name, getattr(student, field.name)) for field in Student._meta.fields
        ]
        student_values.append(dict(values))
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
    column_names = []
    for field in Student._meta.fields:
        column_names.append(field.verbose_name)
    student_dict_list = []
    for student in students:
        key_value_pairs = [
            (field.verbose_name, getattr(student, field.name))
            for field in Student._meta.fields
        ]
        student_dict_list.append(dict(key_value_pairs))

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
    column_names = []
    for field in Representative._meta.fields:
        column_names.append(field.verbose_name)
    representative_dicts_list = []
    for representative in representatives:
        key_value_pairs = [
            (field.verbose_name, getattr(representative, field.name))
            for field in Representative._meta.fields
        ]
        representative_dicts_list.append(dict(key_value_pairs))

    return render(
        request,
        "site_app/student.html",
        {
            "current_student": current_student,
            "representatives": representatives,
            "column_names": column_names,
            "representative_dicts_list": representative_dicts_list,
        },
    )
