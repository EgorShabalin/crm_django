from django.urls import path
from site_app.views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.views.i18n import set_language


app_name = "site_app"

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="site_app/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path("profile/<int:pk>/", profile, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("table/", table, name="table"),
    path("grid/", grid, name="grid"),
    path("tabulator/", tabulator, name="tabulator"),
    path("ag_grid/", ag_grid, name="ag_grid"),
    path("set-language/", set_language, name="set_language"),
]
