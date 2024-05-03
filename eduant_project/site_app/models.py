from django.db import models
from .config import FORM_OF_STUDY, REPRESENTATIVES
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Course Name"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name=_("First Name"),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_("Last Name"),
    )
    middle_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Middle Name"),
    )
    birth_date = models.DateField(
        verbose_name=_("Birth Date"),
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("Course"),
    )
    form_of_study = models.CharField(
        max_length=255,
        choices=FORM_OF_STUDY,
        verbose_name=_("Form Of study"),
    )

    start_date = models.DateField(
        verbose_name=_("Start Date"),
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("End Date"),
    )
    personal_id = models.CharField(
        max_length=255,
        verbose_name=_("Personal ID"),
    )
    personal_id_details = models.CharField(
        max_length=255,
        verbose_name=_("Personal ID details"),
    )
    country = models.CharField(
        max_length=255,
        verbose_name=_("Country"),
    )
    city = models.CharField(
        max_length=255,
        verbose_name=_("City"),
    )
    address = models.CharField(
        max_length=255,
        verbose_name=_("Address"),
    )
    language = models.CharField(
        max_length=255,
        verbose_name=_("Language"),
    )
    phone = models.CharField(
        max_length=255,
        verbose_name=_("Phone"),
    )
    email = models.CharField(
        max_length=255,
        verbose_name=_("Email"),
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Other Contact"),
    )
    debtor = models.BooleanField(
        default=False,
        verbose_name=_("Debtor"),
    )
    active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        if self.middle_name:
            return self.last_name + " " + self.first_name + " " + self.middle_name
        else:
            return self.first_name + " " + self.last_name

    class Meta:
        ordering = ("-created_at",)


class Subject(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Subject Name"),
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("Course"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return str(self.course) + " - " + self.name


class Grade(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    subject = models.CharField(
        max_length=255,
        verbose_name=_("Subject"),
    )
    grade = models.CharField(
        max_length=255,
        verbose_name=_("Grade"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return str(self.student) + " " + self.subject + " " + self.grade


class Internship(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Internship Name"),
    )
    location = models.CharField(
        max_length=255,
        verbose_name=_("Location"),
    )
    result = models.CharField(
        max_length=255,
        verbose_name=_("Result"),
    )
    date_start = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Start Date"),
    )
    date_end = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("End Date"),
    )

    def __str__(self):
        return self.name


class Representative(models.Model):
    student = models.ManyToManyField(
        Student,
        verbose_name=_("Student"),
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name=_("First Name"),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_("Last Name"),
    )
    middle_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Middle Name"),
    )
    birth_date = models.DateField(
        verbose_name=_("Birth Date"),
    )
    personal_id = models.CharField(
        max_length=255,
        verbose_name=_("Personal ID"),
    )
    personal_id_details = models.CharField(
        max_length=255,
        verbose_name=_("Personal ID details"),
    )
    country = models.CharField(
        max_length=255,
        verbose_name=_("Country"),
    )
    city = models.CharField(
        max_length=255,
        verbose_name=_("City"),
    )
    address = models.CharField(
        max_length=255,
        verbose_name=_("Address"),
    )
    language = models.CharField(
        max_length=255,
        verbose_name=_("Language"),
    )
    representative_type = models.CharField(
        choices=REPRESENTATIVES,
        max_length=255,
        verbose_name=_("Representative Type"),
    )
    phone = models.CharField(
        max_length=255,
        verbose_name=_("Phone"),
    )
    email = models.CharField(
        max_length=255,
        verbose_name=_("Email"),
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Other Contact"),
    )
    contractor = models.BooleanField(
        verbose_name=_("Contractor"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        if self.middle_name:
            return self.last_name + " " + self.first_name + " " + self.middle_name
        else:
            return self.first_name + " " + self.last_name


class Contract(models.Model):
    student = models.ManyToManyField(
        Student,
        verbose_name=_("Student"),
    )
    contract_date = models.DateField(
        verbose_name=_("Contract Date"),
    )
    contract_id = models.CharField(
        max_length=255,
        verbose_name=_("Contract ID"),
    )
    contract_price = models.FloatField(
        verbose_name=_("Contract Price"),
    )
    final_settlement_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Final Settlement Date"),
    )
    installment_plan = models.BooleanField(
        verbose_name=_("Installment Plan"),
    )
    discount = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Discount"),
    )
    promotion = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Promotion"),
    )
    contractor = models.ForeignKey(
        Representative,
        on_delete=models.PROTECT,
        verbose_name="Contractor",
    )
    active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return self.contract_id


class Payment(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.PROTECT,
        verbose_name=_("Contract"),
    )
    payment_amount = models.FloatField(
        verbose_name=_("Amount"),
    )
    pay_date = models.DateField(
        verbose_name=_("Pay Date"),
    )
    payed = models.BooleanField(
        verbose_name=_("Payed"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return "Payment" + " " + str(self.payment_amount)


class Document(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    school_leaving_certificate = models.FileField(
        verbose_name=_("School Graduation Certificate"),
    )
    passport = models.FileField(
        verbose_name=_("Passport"),
    )
    form = models.FileField(
        verbose_name=_("Form"),
    )
    application = models.FileField(
        verbose_name=_("Application"),
    )
    photo = models.FileField(
        verbose_name=_("Photo"),
    )
    birth_cert = models.FileField(
        verbose_name=_("Birth Certificate"),
    )
    exit_application = models.FileField(
        verbose_name=_("Exit Application"),
    )
    agreement_for_residence_permit = models.FileField(
        verbose_name=_("Agreement For Residence Permit"),
    )
    medical_cert = models.FileField(
        verbose_name=_("Medical Certificate"),
    )
    hiv_cert = models.FileField(
        verbose_name=_("HIV Certificate"),
    )
    description = models.FileField(
        verbose_name=_("Description"),
    )
    other = models.FileField(
        verbose_name=_("Other"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return "Documents of" + str(self.student)


class Residence_permit(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    arrival_date = models.DateField(
        verbose_name=_("Arrival Date"),
    )
    student_visa = models.BooleanField(
        verbose_name=_("Student Visa"),
    )
    registration_address = models.CharField(
        max_length=255, verbose_name=_("Registration Address")
    )
    residence_permit_id = models.CharField(
        max_length=255,
        verbose_name=_("Residence Permit ID"),
    )
    residence_permit_issue_date = models.DateField(
        verbose_name=_("Residence Permit Issue Date"),
    )
    residence_permit_end_date = models.DateField(
        verbose_name=_("Residence Permit End Date"),
    )
    residence_permit_type = models.CharField(
        max_length=255,
        verbose_name=_("Residence Permit Type"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return self.residence_permit_id


class Order(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    subject = models.CharField(
        max_length=255,
        verbose_name=_("Subject Of Order"),
    )
    order_id = models.CharField(
        max_length=255,
        default=" ",
        verbose_name=_("Order ID"),
    )
    issued_by = models.CharField(
        max_length=255,
        verbose_name=_("Issued By"),
    )
    date_issued = models.DateField(
        verbose_name=_("Issue Date"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return "Order " + str(self.date_issued)


class Statement(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    issued_by = models.CharField(
        max_length=255,
        verbose_name=_("Issued By"),
    )
    submission_to = models.CharField(
        max_length=255,
        verbose_name=_("Submission To"),
    )
    date_issued = models.DateField(
        verbose_name=_("Issue Date"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return "Statement " + self.name + " " + str(self.date_issued)


class Application(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    subject = models.CharField(
        max_length=255,
        verbose_name=_("Subject Of Application"),
    )
    date_issued = models.DateField(
        verbose_name=_("Issue Date"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Time"),
    )

    def __str__(self):
        return "Application " + str(self.date_issued)


class Photo(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    photo = models.ImageField(upload_to="photos/")
