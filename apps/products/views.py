from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from .models import Gorra, Camiseta
from .forms import gorraForm, camisetaForm, gorraUpdateForm, camisetaUpdateForm


### INICIO

def renderInit(request):
    return render(request, 'base.html')

### Productos: Listado y CRUD ###

def product_list(request):

    gorras = Gorra.objects.filter(deleted=False).order_by('-creation_date')
    camisetas = Camiseta.objects.filter(deleted=False).order_by('-creation_date')

    return render(request,'products/product_list.html',{'gorras': gorras, 'camisetas': camisetas})

##Gorras

def createGorra(request):
    gorra = Gorra()
    form = gorraForm(instance=gorra)

    if request.method == "POST":
        form = gorraForm(request.POST, request.FILES, instance=gorra)

        if form.is_valid():
            form.save()
            gorra.current_stock = gorra.initial_stock
            gorra.photo = request.FILES['photo']
            gorra.save()
            return redirect("/products")

    context = {'form': form}
    return render(request, 'products/create_gorra.html', context)

def updateGorra(request, pk):
    gorra = Gorra.objects.get(id=pk)
    form = gorraUpdateForm(instance=gorra)
    if request.method == "POST":
        form = gorraUpdateForm(request.POST, request.FILES, instance=gorra)
        if form.is_valid():
            form.save()
            return redirect("/products")
    context = {'form': form}
    return render(request, 'products/update_gorra.html', context)

def deleteGorra(request, pk):
    gorra = Gorra.objects.get(id=pk)
    if request.method == "POST":
        gorra.deleted = True
        gorra.save()
        return redirect("/products")
    context = {'item': gorra}
    return render(request, 'products/delete_gorra.html', context)

##Camisetas

def createCamiseta(request):
    camiseta = Camiseta()
    form = camisetaForm(instance=camiseta)

    if request.method == "POST":
        form = camisetaForm(request.POST, request.FILES, instance=camiseta)
        
        if form.is_valid():
            form.save()
            camiseta.photo = request.FILES['photo']
            camiseta.current_stock = camiseta.initial_stock
            camiseta.save()
            return redirect("/products")
            
    context = {'form': form}
    return render(request, 'products/create_camiseta.html', context)

def updateCamiseta(request, pk):
    camiseta = Camiseta.objects.get(id=pk)
    form = camisetaUpdateForm(instance=camiseta)
    if request.method == "POST":
        form = camisetaUpdateForm(request.POST, request.FILES, instance=camiseta)
        if form.is_valid():
            form.save()
            return redirect("/products")
    context = {'form': form}
    return render(request, 'products/update_camiseta.html', context)

def deleteCamiseta(request, pk):
    camiseta = Camiseta.objects.get(id=pk)
    if request.method == "POST":
        camiseta.deleted = True
        camiseta.save()
        return redirect("/products")
    context = {'item': camiseta}
    return render(request, 'products/delete_camiseta.html', context)
