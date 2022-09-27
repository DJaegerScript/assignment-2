# TODO: Implement Routings Here

from venv import create
from django.urls import path

from todolist.views import create_todolist, delete_todolist, login_todolist, logout_todolist, register_todolist, show_todolist


app_name = 'todolist'

urlpatterns= [
    path('', show_todolist, name="show_todolist"),
    path('login', login_todolist, name="login_todolist"),
    path('register', register_todolist, name="register_todolist"),
    path('logout', logout_todolist, name="logout_todolist"),
    path('task', create_todolist, name="create_todolist"),
    path('task/<int:id>', create_todolist, name="update_todolist"),
    path('delete-task/<int:id>', delete_todolist, name="delete_todolist"),
]