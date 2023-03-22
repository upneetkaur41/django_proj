"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
from myapp.views import create_blog,list_blogs,delete_blog,update_blog
from Market.views import products_available,list_of_products,add_to_cart,remove_from_cart,home_page,create_new_user,login_user

urlpatterns = [
    path('',home_page,name='HomePage'),
    path('admin/', admin.site.urls),
    path('blog/create',create_blog),
    path('blog/list',list_blogs),
    path('blog/<int:pk>/delete/',delete_blog),
    path('display/products_available',products_available),
    path('display/list_of_products',list_of_products,name='list'),
    path('display/<int:pk>/add_to_cart',add_to_cart,name='cart'),
    path('display/<int:pk>/remove_from_cart',remove_from_cart),
    path('newUser/create_new_user',create_new_user,name='newUser'),
    path('newUser/login_user',login_user,name='loginUser')

]
