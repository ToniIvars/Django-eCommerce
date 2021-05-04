from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('view-profile/<str:profile>', views.view_profile, name='view_profile'),
    path('product/<product_name>', views.product, name='product'),
    path('create-product', views.create_product, name='create_product'),
    path('edit-product/<product_name>', views.edit_product, name='edit_product'),
    path('delete-product/<product_name>', views.delete_product, name='delete_product'),
    path('my-products', views.my_products, name='my_products'),
    path('search', views.search, name='search'),
    path('buy/<product_name>', views.buy, name='buy'),
    path('orders', views.orders, name='orders'),
    path('add-to-cart/<product_name>', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('change-quantity', views.change_quantity, name='change_quantity'),
    path('delete-from-cart', views.delete_from_cart, name='delete_from_cart'),
    path('view-order/<int:id>', views.view_order, name='view_order'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)