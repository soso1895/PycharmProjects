"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book import views as book_views
from django.http import HttpResponse

#
# def index(request):
#     return HttpResponse("tu shu shou  ye ")


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', index),
    # path('book/', views.book),
    # path('book/detail/<book_id>/', views.book_detail),
    # path('book/author/', views.author_detail)
    path('', include('front.urls')),
    path('cms/', include('cms.urls')),
    path('book/', book_views.book)

]
