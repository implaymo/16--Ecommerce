from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/signup/", views.account_signup, name="account_signup"),
    path("accounts/login/", views.account_login, name="account_login")
]

