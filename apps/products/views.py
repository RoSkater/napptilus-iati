import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Gorra, Camiseta
from .forms import gorraForm, camisetaForm, gorraUpdateForm, camisetaUpdateForm

from django.views.decorators.csrf import csrf_exempt

### INICIO

def renderInit(request):
    return render(request, 'base.html')

### Productos: Listado y CRUD ###

def product_list(request):

    gorras = Gorra.objects.filter(deleted=False).order_by('-creation_date')
    camisetas = Camiseta.objects.filter(deleted=False).order_by('-creation_date')

    if 'Mozilla' in request.META.get('HTTP_USER_AGENT', '') or \
       'Chrome' in request.META.get('HTTP_USER_AGENT', '') or \
       'Safari' in request.META.get('HTTP_USER_AGENT', ''): 
        return render(request,'products/product_list.html',{'gorras': gorras, 'camisetas': camisetas})
    
    else:
        gorra_list = list(gorras.values())
        camiseta_list = list(camisetas.values())
        return JsonResponse({'Gorras': gorra_list, 'Camisetas': camiseta_list})

##Gorras

@csrf_exempt
def createGorra(request):
    gorra = Gorra()
    form = gorraForm(instance=gorra)

    if request.method == "POST":
        form = gorraForm(request.POST, request.FILES, instance=gorra)

        if 'Mozilla' in request.META.get('HTTP_USER_AGENT', '') or \
       'Chrome' in request.META.get('HTTP_USER_AGENT', '') or \
       'Safari' in request.META.get('HTTP_USER_AGENT', ''): 

            if form.is_valid():
                form.save()
                gorra.current_stock = gorra.initial_stock
                gorra.save()
                return redirect("/products")
                
        else:
            data = json.loads(request.body)
            gorra = Gorra(**data)
            gorra.save()
            return JsonResponse({'message': 'Item created'})

    context = {'form': form}
    return render(request, 'products/create_gorra.html', context)

@csrf_exempt
def updateGorra(request, pk):
    gorra = Gorra.objects.get(id=pk)
    form = gorraUpdateForm(instance=gorra)
    if request.method == "POST":
        form = gorraUpdateForm(request.POST, request.FILES, instance=gorra)
        if form.is_valid():
            form.save()
            return redirect("/products")

    elif request.method == 'PUT':
        instance = Gorra.objects.get(id=pk)
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return JsonResponse({'message': 'Fields updated'})
    
    context = {'form': form}
    return render(request, 'products/update_gorra.html', context)

@csrf_exempt
def deleteGorra(request, pk):
    gorra = Gorra.objects.get(id=pk)
    if request.method == "POST":
        gorra.deleted = True
        gorra.save()
        return redirect("/products")
    
    elif request.method == "DELETE":
        gorra.deleted = True
        gorra.save()
        return JsonResponse({'message': f'Gorra {pk} deleted'})

    context = {'item': gorra}
    return render(request, 'products/delete_gorra.html', context)

##Camisetas
@csrf_exempt
def createCamiseta(request):
    camiseta = Camiseta()
    form = camisetaForm(instance=camiseta)

    if request.method == "POST":
        form = camisetaForm(request.POST, request.FILES, instance=camiseta)
        if 'Mozilla' in request.META.get('HTTP_USER_AGENT', '') or \
       'Chrome' in request.META.get('HTTP_USER_AGENT', '') or \
       'Safari' in request.META.get('HTTP_USER_AGENT', ''): 

            if form.is_valid():
                form.save()
                camiseta.current_stock = camiseta.initial_stock
                camiseta.save()
                return redirect("/products")
        
        else:
            data = json.loads(request.body)
            camiseta = Camiseta(**data)
            camiseta.save()
            return JsonResponse({'message': 'Item created'})

            
    context = {'form': form}
    return render(request, 'products/create_camiseta.html', context)

@csrf_exempt
def updateCamiseta(request, pk):
    camiseta = Camiseta.objects.get(id=pk)
    form = camisetaUpdateForm(instance=camiseta)
    if request.method == "POST":
        form = camisetaUpdateForm(request.POST, request.FILES, instance=camiseta)
        if form.is_valid():
            form.save()
            return redirect("/products")
    
    elif request.method == 'PUT':
        instance = Camiseta.objects.get(id=pk)
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return JsonResponse({'message': 'Fields updated'})

    context = {'form': form}
    return render(request, 'products/update_camiseta.html', context)

@csrf_exempt
def deleteCamiseta(request, pk):
    camiseta = Camiseta.objects.get(id=pk)
    if request.method == "POST":
        camiseta.deleted = True
        camiseta.save()
        return redirect("/products")
    
    elif request.method == "DELETE":
        camiseta.deleted = True
        camiseta.save()
        return JsonResponse({'message': f'Camiseta {pk} deleted'})


    context = {'item': camiseta}
    return render(request, 'products/delete_camiseta.html', context)

