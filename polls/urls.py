from django.urls import path
from allauth.account.views import LogoutView, LoginView, SignupView
from allauth.mfa.views import AuthenticateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/signup/", SignupView.as_view(),  name="account_signup"),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path("accounts/logout/", LogoutView.as_view(), name="account_logout"),
    path('accounts/2fa/', AuthenticateView.as_view() , name="account_2fa"),
    path('search', views.search, name="search"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path('update_bill/', views.update_bill, name="update_bill"),
    path('delete_item/', views.delete_item, name="delete_item"),
    path('checkout/', views.checkout, name="checkout"),
    path('cancel_checkout/', views.cancel_checkout, name="cancel_checkout"),
    path('success_checkout/', views.success_checkout, name="success_checkout" ),
    path('account_settings/', views.account_settings, name='account_settings'),
]

