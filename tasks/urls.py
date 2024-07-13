from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/start/', views.task_start_session, name='task_start_session'),
    path('task/<int:pk>/end/<int:session_pk>/', views.task_end_session, name='task_end_session'),
    path('task/<int:pk>/complete/', views.task_complete, name='task_complete'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete')

]
