from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from .forms import ProductoForm, MarcaForm
from .models import Producto, Marca

def home(request):
    return render(request, 'home.html')

def productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query), eliminado=False)
    else:
        productos = Producto.objects.filter(eliminado=False)
    return render(request, 'product_list.html', {'productos': productos})

def create_product(request):
    if request.method == 'GET':
        return render(request, 'create_product.html', {
            'form': ProductoForm()
        })
    else:
        try:
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('product_list')
            else:
                return render(request, 'create_product.html', {
                    'form': form,
                    'error': 'Datos incorrectos'
                })
        except Exception as e:
            return render(request, 'create_product.html', {
                'form': form,
                'error': f'Error al guardar el producto: {e}'
            })

def delete_product(request, id):
    product = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        product.eliminado = True
        product.fecha_eliminacion = timezone.now()
        product.save()
        return redirect('product_list')

def update_product(request, id):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, pk=id)
        form = ProductoForm(instance=producto)
        return render(request, 'update_producto.html', {
            'producto': producto,
            'form': form
        })
    else:
        try:
            producto = get_object_or_404(Producto, pk=id)
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('product_list')
            else:
                return render(request, 'update_producto.html', {
                    'producto': producto,
                    'form': form,
                    'error': 'Datos incorrectos'
                })
        except ValueError:
            return render(request, 'update_producto.html', {
                'producto': producto,
                'form': form,
                'error': 'No se puede actualizar'
            })

def marcas(request):
    query = request.GET.get('q')
    if query:
        marcas = Marca.objects.filter(Q(nombre__icontains=query), eliminado=False)
    else:
        marcas = Marca.objects.filter(eliminado=False)
    return render(request, 'marca_list.html', {'marcas': marcas})

def create_marca(request):
    if request.method == 'GET':
        return render(request, 'create_marca.html', {
            'form': MarcaForm()
        })
    else:
        try:
            form = MarcaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('marca_list')
            else:
                return render(request, 'create_marca.html', {
                    'form': form,
                    'error': 'Datos incorrectos'
                })
        except Exception as e:
            return render(request, 'create_marca.html', {
                'form': form,
                'error': f'Error al guardar la marca: {e}'
            })

def delete_marca(request, id):
    marca = get_object_or_404(Marca, pk=id)
    if marca.productos.filter(eliminado=False).exists():
        return render(request, 'marca_list.html', {
            'marcas': Marca.objects.filter(eliminado=False),
            'error': 'No se puede eliminar la marca porque tiene productos asociados'
        })
    if request.method == 'POST':
        marca.eliminado = True
        marca.fecha_eliminacion = timezone.now()
        marca.save()
        return redirect('marca_list')

def update_marca(request, id):
    if request.method == 'GET':
        marca = get_object_or_404(Marca, pk=id)
        form = MarcaForm(instance=marca)
        return render(request, 'update_marca.html', {
            'marca': marca,
            'form': form
        })
    else:
        try:
            marca = get_object_or_404(Marca, pk=id)
            form = MarcaForm(request.POST, instance=marca)
            if form.is_valid():
                form.save()
                return redirect('marca_list')
            else:
                return render(request, 'update_marca.html', {
                    'marca': marca,
                    'form': form,
                    'error': 'Datos incorrectos'
                })
        except ValueError:
            return render(request, 'update_marca.html', {
                'marca': marca,
                'form': form,
                'error': 'No se puede actualizar'
            })