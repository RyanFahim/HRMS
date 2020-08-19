from django.urls import path
from . import views

urlpatterns = [
    path("asset",views.asset_list, name='asset_list'),
    path("asset_form",views.asset_form, name='asset_form'),
    path("delete/<int:id>/",views.asset_delete, name='asset_delete'),
]