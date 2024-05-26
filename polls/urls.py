from django.urls import path
from allauth.account.views import LogoutView, LoginView, SignupView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/signup/", SignupView.as_view(),  name="account_signup"),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path("accounts/logout/", LogoutView.as_view(), name="account_logout"),
    path('search', views.search, name="search"),
    path('cart_products/<int:product_id>/', views.cart_products, name="cart_products"),
    path('delete_cart', views.delete_cart, name='delete_cart')
]

