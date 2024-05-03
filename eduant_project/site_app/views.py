from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .forms import SignupForm, EditUserForm
from .models import *
from custom_user.models import User

from datetime import *

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def index(request):
    return render(request, "site_app/index.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _("You Have Been Logged In!"))
            return redirect("site_app:index")
        else:
            messages.success(
                request, _("There Was An Error Logging In, Please Try Again...")
            )
            return redirect("site_app:login")

    else:
        return render(request, "site_app/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, _("You Have Been Logged Out..."))
    return redirect("site_app:login")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, _("You Have Been Signed Up!"))
            return redirect("site_app:login")

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
            messages.success(request, _("Profile Has Been Updated!"))
            return redirect("site_app:login")

        return render(request, "site_app/edit_profile.html", {"form": form})


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
    # print(result)
    return result


def check_debt(request):
    payments = Payment.objects.all()

    today = datetime.today()
    # print(f"n/ TODAY: {today}/n")

    for payment in payments:
        # print(f"n/ PAY DATE: {payment.pay_date}/n")
        if payment.pay_date < today.date() and payment.payed == False:
            for s in payment.contract.student.all():
                if s.debtor == False:
                    s.debtor = True
                    s.save()
                messages.success(request, _("There Are New Debts!"))
            return redirect("site_app:ag_grid")
        elif payment.pay_date < today.date() and payment.payed == True:
            for s in payment.contract.student.all():
                s.debtor = False
                s.save()
            return redirect("site_app:ag_grid")
        else:
            messages.success(request, _("No New Debts!"))
            return redirect("site_app:ag_grid")


def hand_over(request, pk):
    statement = Statement.objects.get(id=pk)

    today = datetime.today()

    if statement.handed_over_date:

        return messages.success(
            request,
            _("The Document Has Been Handed Over Already!"),
        )
    else:
        statement.handed_over_date = today
        statement.save()
        messages.success(request, _(f"The Document Has Been Handed Over Now!"))
        return redirect(f"/statements/{statement.student.id}")


@login_required
def ag_grid(request):
    students = Student.objects.all()

    content = create_grid_content(Student, students)
    column_names = content[0]
    student_dict_list = content[1]

    column_names.insert(5, "Contract")
    for i in student_dict_list:
        i.update({"Contract": Contract.objects.filter(student=i["ID"]).first()})

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
    photos = Photo.objects.filter(student=current_student)
    representatives = Representative.objects.filter(student=current_student)
    contracts = Contract.objects.filter(student=current_student)
    courses = Course.objects.filter(id=current_student.id)
    residence_permit = Residence_permit.objects.get(student=current_student)
    payments = Payment.objects.all()
    debt = 0
    debt_date = None
    for payment in payments:
        for s in payment.contract.student.all():
            if s == current_student:
                debt = debt + payment.payment_amount
                debt_date = payment.pay_date

    return render(
        request,
        "site_app/student.html",
        {
            "current_student": current_student,
            "photos": photos,
            "representatives": representatives,
            "contracts": contracts,
            "courses": courses,
            "residence_permit": residence_permit,
            "debt": debt,
            "debt_date": debt_date,
        },
    )


@login_required
def representatives(request, pk):
    current_student = Student.objects.get(id=pk)
    representatives = Representative.objects.filter(student=current_student)

    representatives_content = create_grid_content(Representative, representatives)
    representatives_columns = representatives_content[0]
    representative_dicts_list = representatives_content[1]

    return render(
        request,
        "site_app/representatives.html",
        {
            "current_student": current_student,
            "representatives": representatives,
            "representatives_columns": representatives_columns,
            "representative_dicts_list": representative_dicts_list,
        },
    )


@login_required
def representatives_all(request):
    representatives = Representative.objects.all()

    representatives_content = create_grid_content(Representative, representatives)
    representatives_columns = representatives_content[0]
    representative_dicts_list = representatives_content[1]

    return render(
        request,
        "site_app/representatives_all.html",
        {
            "representatives": representatives,
            "representatives_columns": representatives_columns,
            "representative_dicts_list": representative_dicts_list,
        },
    )


@login_required
def representative(request, pk):
    representative = Representative.objects.get(id=pk)
    students = Student.objects.filter(representative=representative)
    contracts = Contract.objects.filter(contractor=representative)

    return render(
        request,
        "site_app/representative.html",
        {
            "representative": representative,
            "students": students,
            "contracts": contracts,
        },
    )


@login_required
def contracts(request):
    contracts = Contract.objects.all()
    contracts_content = create_grid_content(Contract, contracts)
    contracts_columns = contracts_content[0]
    contracts_dicts_list = contracts_content[1]

    return render(
        request,
        "site_app/contracts.html",
        {
            "contracts": contracts,
            "contracts_columns": contracts_columns,
            "contracts_dicts_list": contracts_dicts_list,
        },
    )


@login_required
def payments(request, pk):
    contract = Contract.objects.get(id=pk)
    payments = Payment.objects.filter(contract=contract)
    students = contract.student.all()
    representatives = Representative.objects.all()
    current_representatives = []
    for student in students:
        for representative in representatives:
            if representative.student == student:
                current_representatives.append(representative)

    return render(
        request,
        "site_app/payments.html",
        {
            "contract": contract,
            "payments": payments,
            "students": students,
            "current_representatives": current_representatives,
        },
    )


@login_required
def course(request, pk):
    current_course = Course.objects.get(id=pk)
    subjects = Subject.objects.filter(course=current_course)

    return render(
        request,
        "site_app/course.html",
        {
            "current_course": current_course,
            "subjects": subjects,
        },
    )


@login_required
def courses(request):
    courses = Course.objects.all()

    return render(
        request,
        "site_app/courses.html",
        {
            "courses": courses,
        },
    )


@login_required
def documents(request, pk):
    current_student = Student.objects.get(id=pk)
    docs = Document.objects.filter(student=current_student)

    return render(
        request,
        "site_app/documents.html",
        {
            "current_student": current_student,
            "docs": docs,
        },
    )


@login_required
def orders(request, pk):
    current_student = Student.objects.get(id=pk)
    orders = Order.objects.filter(student=current_student)

    return render(
        request,
        "site_app/orders.html",
        {
            "current_student": current_student,
            "orders": orders,
        },
    )


def generate_pdf(request, pk):
    order = Order.objects.get(id=pk)
    template_path = "site_app/order_for_enrollment.html"
    context = {"order": order}
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="generated_pdf.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error Generating PDF")

    return response


@login_required
def statements(request, pk):
    current_student = Student.objects.get(id=pk)
    statements = Statement.objects.filter(student=current_student)

    return render(
        request,
        "site_app/statements.html",
        {
            "current_student": current_student,
            "statements": statements,
        },
    )


@login_required
def applications(request, pk):
    current_student = Student.objects.get(id=pk)
    applications = Application.objects.filter(student=current_student)

    return render(
        request,
        "site_app/applications.html",
        {
            "current_student": current_student,
            "applications": applications,
        },
    )


@login_required
def grades(request, pk):
    current_student = Student.objects.get(id=pk)
    grades = Grade.objects.filter(student=current_student)

    return render(
        request,
        "site_app/grades.html",
        {
            "current_student": current_student,
            "grades": grades,
        },
    )


@login_required
def internships(request, pk):
    current_student = Student.objects.get(id=pk)
    internships = Internship.objects.filter(student=current_student)

    return render(
        request,
        "site_app/internships.html",
        {
            "current_student": current_student,
            "internships": internships,
        },
    )
