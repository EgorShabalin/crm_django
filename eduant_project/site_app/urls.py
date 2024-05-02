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
    path("ag_grid/", ag_grid, name="ag_grid"),
    path("student/<int:pk>/", student, name="student"),
    path("set-language/", set_language, name="set_language"),
    path("representatives/<int:pk>/", representatives, name="representatives"),
    path("representatives_all/", representatives_all, name="representatives_all"),
    path("representative/<int:pk>/", representative, name="representative"),
    path("contracts/", contracts, name="contracts"),
    path("payments/<int:pk>/", payments, name="payments"),
    path("course/<int:pk>/", course, name="course"),
    path("courses/", courses, name="courses"),
    path("documents/<int:pk>/", documents, name="documents"),
    path("orders/<int:pk>/", orders, name="orders"),
    path("statements/<int:pk>/", statements, name="statements"),
    path("applications/<int:pk>/", applications, name="applications"),
    path("grades/<int:pk>/", grades, name="grades"),
    path("internships/<int:pk>/", internships, name="internships"),
    path("check_debt/", check_debt, name="check_debt"),
    path("generate_pdf/<int:pk>/", generate_pdf, name="generate_pdf"),
]
