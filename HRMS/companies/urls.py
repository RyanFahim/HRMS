from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.CompanyView.as_view(), name = 'company_view'),
    # path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('create/', views.CreateCompany.as_view(), name='create_company'),
    path('update/', views.UpdateCompany.as_view(), name='update_company'),
    # path('ajax/crud/delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('delete/', views.DeleteCompany.as_view(), name='delete_company'),
    path('account/',  views.account, name='account'),
]