from django.urls import path
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('',views.TaskList.as_view(),name='task_list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(),name='task_detail'),
    path('task_create/',views.TaskCreate.as_view(),name='task_create'),
    path('task_update/<int:pk>/',views.TaskUpdate.as_view(),name='task_update')
]


