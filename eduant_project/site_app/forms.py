from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "phone", "password1", "password2")

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": _("Your Email")})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your Phone")})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": _("Your Password")})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": _("Repeat Password")})
    )


class EditUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "phone", "password1", "password2")

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your First name")})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your Last name")})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": _("Your Email")})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your Phone")})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": _("Your Password")})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": _("Repeat Password")})
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your Email")})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": _("Your Password")})
    )
