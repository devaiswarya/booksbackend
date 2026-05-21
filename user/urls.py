from django.urls import path
from .views import create_user,get_user,get_users,Update_user,delete_user,login_user

urlpatterns=[
    path('create',create_user,name="create_user"),
    path('getuser',get_users,name="get_users"),
    path('getdata/<int:pk>',get_user,name="get_user"),
    path('update/<int:pk>',Update_user,name='update_user'),
    path('delete/<int:pk>',delete_user,name="delete_user"),
    path('gets',login_user,name='login_user')
]