from django.urls import path

from . import views


urlpatterns = [
    path('', views.AllTodos.as_view(), name='tasks_list'),
    path('add/', views.AddTodo.as_view(), name='add_todo'),
    path('update/<int:pk>', views.UpdateTodo.as_view(), name='update_todo'),
    path('delete/<int:pk>', views.DeleteTodo.as_view(), name='delete_todo')
]