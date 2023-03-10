from django.urls import path, include
from . import views

urlpatterns = [

    path("", views.index, name='index'),
    path('show_books', views.show_books, name='show_books'),
    path('show_users', views.show_users, name='show_users'),
    path('records', views.records, name='records'),
    path('add_book', views.add_book, name='add_book'),
    path('add_user', views.add_user, name='add_user'),
    path('add_record', views.add_record, name='add_record'),
    # path('add_book/<int:book_id>', views.records, name='records')

]
