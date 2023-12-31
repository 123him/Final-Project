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
   
    path('viewFood_items/<str:restaurant_name>',views.viewFooditems),
    path('chef/',views.chef),
    path('reservation/',views.reservation),
    path('account/',views.account),
    path('login1/',views.login1),
    path('account2/',views.account2),
   
    path('viewadmin_restaurant/',views.viewadmin_restaurant),
    path('adminupdate_restaurant/<int:id>',views.adminupdate_restaurant),
    path('update1/<int:id>',views.update1),
    path('admin_deleteRestaurant/<int:id>',views.admin_deleteRestaurant),
    path('res_view_foodMenu/',views.res_view_foodMenu),
    path('res_update_foodMenu/<int:id>',views.res_update_foodMenu),
    path('res_update_foodMenu1/<int:id>',views.res_update_foodMenu1),
    path('res_delete_foodMenu/<int:id>',views.res_delete_foodMenu),
    path('res_offer/',views.res_offer),
    path('offer1/',views.offer1),
    path('res_view_foodItem/',views.res_view_foodItem),
    path('res_update_foodItem/<int:id>',views.res_update_foodItem),
    path('res_update_foodItem1/<int:id>',views.res_update_foodItem1),
    path('res_delete_foodItem/<int:id>',views.res_delete_foodItem),
    path('user_view_offer/',views.user_view_offer),
    path('user_details/',views.user_details),
    path('rest/',views.public_restaurant),
    path('offers/',views.public_offers),
    path('res_view_offers/',views.res_view_offers),
    path('res_update_offers/<int:id>',views.res_update_offers),
    path('offer2/<int:id>',views.offer2),
    path('res_delete_offers/<int:id>',views.res_delete_offers),
    path('cart/<int:id>',views.cart),
    path('cart1/',views.cart1),
    path('viewcart/',views.viewcart),
    path('order/<int:id>',views.order),
    path('order1/',views.order1),
    path('view_restaurant/',views.viewRestaurant),
    path('user_view_order/',views.user_view_order),
    path('userconfirm_order/',views.userconfirm_order),
    path('usercancelled_order/',views.usercanceled_order),
    path('resview_order/',views.resview_order),
    path('order_confirm/<int:id>',views.orderconf),
    path('order_delete/<int:id>',views.orderdel),
    path('resconfirm_order/',views.resconfirm_order),
    path('rescanceled_order/',views.rescanceled_order),
    path('out_delivery/<int:id>',views.out_for_delivery)
   
    # path('cancelled_order/',views.cancel_order),
    
   
   
 
   
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)