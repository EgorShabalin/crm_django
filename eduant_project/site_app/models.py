from django.db import models
from .config import FORM_OF_STUDY, REPRESENTATIVES
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name=_("First name"),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_("Last name"),
    )
    middle_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Middle name"),
    )
    birth_date = models.DateField(
        verbose_name=_("Birth date"),
    )
    personal_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Personal ID"),
    )
    residence_permit_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Residence Permit ID"),
    )
    residence_permit_end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Residence Permit End Date"),
    )

    date_enroll = models.DateField(
        verbose_name=_("Date of enrollment"),
    )
    payer = models.BooleanField(
        verbose_name=_("Contractor"),
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
        blank=True,
        null=True,
        verbose_name=_("Address"),
    )
    language = models.CharField(
        max_length=255,
        verbose_name=_("Language"),
    )
    form_of_study = models.CharField(
        choices=FORM_OF_STUDY,
        max_length=255,
        verbose_name=_("Form of study"),
    )
    contract_date = models.DateField(
        verbose_name=_("Contract date"),
    )
    contract_id = models.CharField(
        max_length=255,
        verbose_name=_("Contract id"),
    )
    contract_price = models.CharField(
        max_length=255,
        verbose_name=_("Contract price"),
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
    find_out = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Where found out"),
    )
    agent_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Agent name"),
    )
    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Phone"),
    )
    email = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Email"),
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Other contact"),
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
        verbose_name=_("Created time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated time"),
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ("-created_at",)


class Course(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Course name"),
    )
    student = models.ManyToManyField(Student)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated time"),
    )

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        verbose_name=_("Course"),
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
        verbose_name=_("Created time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated time"),
    )

    def __str__(self):
        return str(self.course) + " " + self.subject + " " + self.grade


class Representative(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name=_("Student"),
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("First name"),
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Last name"),
    )
    middle_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Middle name"),
    )
    personal_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Personal ID"),
    )
    country = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Country"),
    )
    city = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("City"),
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Address"),
    )
    representative_type = models.CharField(
        choices=REPRESENTATIVES,
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Representative type"),
    )
    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Phone"),
    )
    email = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Email"),
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Other contact"),
    )
    payer = models.BooleanField(
        verbose_name=_("Contractor"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created time"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated time"),
    )

    def __str__(self):
        return self.first_name + " " + self.last_name
