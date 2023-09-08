"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('menu/',views.menu),
    path('admin1/',views.admin1),
    path('user1/',views.user1),
    path('res/',views.restur),
    path('login/',views.login),
    path('table/',views.table),
    path('create_restaurant/',views.create_restaurant),
    path('userHome/',views.userHome),
    path('restaurentHome/',views.restaurentHome),
    path('addFood/',views.addFood),
    path('food_menu/',views.foodmenu1),
    path('addItem/',views.items),
    path('food_item/',views.item1),
    path('view_restaurant/',views.viewRestaurant),
    path('viewFood_items/',views.viewFooditems),
    
   path('chef/',views.chef),
   path('reservation/',views.reservation),
    
    path('account/',views.account),
    path('login1/',views.login1),
    path('account2/',views.account2)
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)