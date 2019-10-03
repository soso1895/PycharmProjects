from django.urls import path
from . import views
from book import views as book_views

app_name = 'front'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('login/', views.login, name='login'),
#     path('book/', views.book, name='book'),
#     path('movie/', views.movie, name='movie'),
#     path('city/', views.city, name='city'),
#     path('book/detail/<book_id>/', views.book_detail, name='detail'),
#
# ]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('company/', views.company, name='company'),
#     path('school/', views.school, name='school'),
#
#
# ]

urlpatterns = [
    path('', views.index, name='index'),

]
