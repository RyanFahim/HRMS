from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login",views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("employee",views.employee_list, name='employee_list'),
    path("form",views.employee_form, name='employee_form'),
    path("delete/<int:id>/",views.employee_delete, name='employee_delete'),
    path("<int:id>/",views.employee_form, name='employee_update'),
    #about
    path("login/about", views.about, name='about'),
    #training
    path("training/", views.training, name='training'),
    path("complain/", views.complain, name='complain'),
    path("complain/delete/<int:id>/", views.complain_delete, name='complain_delete'),
    path("login/price", views.price, name='price'),
    path("login/communication", views.communication, name='communication'),
    #asset
    path('award/',views.award, name='award'),
    path('login/attendence/', views.attendence, name='attendence'),
    path('login/empAward', views.empAward, name='empAward'),
    path('login/noticeEmployee', views.noticeEmployee, name='noticeEmployee'),
    #CV
    path('login/cv', views.cv, name='cv'),
    path('upload/', views.cv),
    path('candidate', views.candidate, name='candidate'),
    #Maps
    path("login/map", views.map, name='map')
    
]