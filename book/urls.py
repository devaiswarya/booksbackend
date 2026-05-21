from django.urls import path
from .views import create_user_book,get_user_book,update_user_book,get_book,delete_user_book

urlpatterns=[
    path('create',create_user_book,name='create_user_book'),
    path('fetched',get_user_book,name='get_user_book'),
    path('upadte/<int:pk>',update_user_book,name='update_user_book'),
    path('getdata/<int:pk>',get_book,name="get_book"),
    path("deletedata/<int:pk>",delete_user_book,name="delete_user_book")
]