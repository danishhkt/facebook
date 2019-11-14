from django.urls import path
from . import views 
urlpatterns = [
    path('login',views.fn_test),
    path('register/',views.fn_register)
]