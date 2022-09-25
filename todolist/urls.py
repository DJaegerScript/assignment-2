# TODO: Implement Routings Here

from venv import create
from django.urls import path

from todolist.views import create_todolist, login_todolist, logout_todolist, register_todolist, show_todolist


app_name = 'todolist'

urlpatterns= [
    path('', show_todolist, name="show_todolist"),
    path('login', login_todolist, name="login_todolist"),
    path('register', register_todolist, name="register_todolist"),
    path('logout', logout_todolist, name="logout_todolist"),
    path('create-task', create_todolist, name="create_todolist"),
]