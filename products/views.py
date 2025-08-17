'''Products app views'''
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import Product
from .forms import ProductForm

def all_products(request):
    '''View to return products page'''

    products = Product.objects.all() # pylint: disable=E1101

    context = {
        'products':products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    '''Returns details for single product'''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_detail.html', context)

def add_product(request):
    '''Add a product to the store'''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
