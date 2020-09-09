from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.NoticeView.as_view(), name='notice_view'),
    # path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('create/', views.CreateNotice.as_view(), name = 'create_notice' ),
    path('delete/', views.DeleteNotice.as_view(), name="delete_notice"),
    path("update/", views.UpdateNotice.as_view(), name="update_notice")
]