from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login",views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("employee",views.employee_list, name='employee_list'),
    path("form",views.employee_form, name='employee_form'),
    path("delete/<int:id>/",views.employee_delete, name='employee_delete'),

    
]