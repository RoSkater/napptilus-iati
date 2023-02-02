"""napptilus_iati URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from apps.products.views import renderInit, product_list, createGorra, updateGorra, deleteGorra, \
createCamiseta, updateCamiseta, deleteCamiseta
from apps.cart.views import addToCart, displayCart, buyCart

urlpatterns = [
    path('', renderInit, name="init"),
    path('admin/', admin.site.urls),
    path('products/', product_list, name="products"),
    path('products/create/gorra', createGorra, name='create_gorra'),
    path('products/update/gorra/<int:pk>', updateGorra, name='update_gorra'),
    path('products/delete/gorra/<int:pk>', deleteGorra, name='delete_gorra'),
    path('products/create/camiseta', createCamiseta, name='create_camiseta'),
    path('products/update/camiseta/<int:pk>', updateCamiseta, name='update_camiseta'),
    path('products/delete/camiseta/<int:pk>', deleteCamiseta, name='delete_camiseta'),
    path('products/add_to_cart/<int:pk>', addToCart, name='add_to_cart'),
    path('cart/', displayCart, name='cart'),
    path('cart/buy', buyCart, name='buy_cart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
