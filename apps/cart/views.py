from django.shortcuts import render, redirect

from .models import OrderProduct, Cart

from ..products.models import Product, Gorra, Camiseta

# Create your views here.

def addToCart(request, pk):
    product = Product.objects.filter(id=pk).first()
    order_product, status = OrderProduct.objects.get_or_create(product=product)
    cart, status = Cart.objects.get_or_create()

    if request.method == "POST":

        order_product.quantity = int(request.POST.get("quantity"))
        if product.current_stock < 1:
            return render(request, 'orders/out_of_stock.html',{'product': product})
    
        elif product.current_stock < order_product.quantity:
            return render(request, 'orders/out_of_stock.html',{'product': product})

        else:
            cart.products.add(order_product)
            product.current_stock -= order_product.quantity
            order_product.save()
            product.save()
            return redirect('/cart')
    
   
    return render(request, 'orders/add_to_cart.html', {'product': product})

def displayCart(request):
    cart, status = Cart.objects.get_or_create()
    return render(request, 'orders/cart.html', {'cart': cart})

def buyCart(request):
    if request.method == "POST":
        cart = Cart.objects.get()
        order = OrderProduct.objects.all()
        cart.delete()
        order.delete()
        return redirect('/cart')

    return render(request, 'orders/confirm_order.html')