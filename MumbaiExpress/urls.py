from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name="index"),
    path('aboutus',views.Aboutus.as_view(),name="aboutus"),
    path('contactus',views.Contactus.as_view(),name="contactus"),
    path('services',views.Services.as_view(),name="services"),
    path('orders',views.Orders.as_view(),name="orders"),
    path('signup',views.Signup.as_view(),name="signup"),
    path('login',views.Login.as_view(),name="login"),
    path('logout',views.logout,name="logout"),
    path('ordertable',views.Ordertable,name="ordertable"),
    path('orders',views.Radio.as_view(),name="orders"),
    path('delete/<int:eid>',views.Delete,name="delete"),
    path('courier',views.Courier.as_view(),name="courier"),
    path('payments',views.Payment.as_view(),name="Payments"),
]