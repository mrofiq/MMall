from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ecommerce import forms
from .models import Product



#
# Views handlers
#
def index(request):
    product_list = Product.objects.all()
    context = {
        'products': product_list
    }
    return render(request, "ecommerce/index.html", context)


def detail(request, id):
    product = Product.objects.get(pk=id)
    context = {
        'product': product
    }
    return render(request, "ecommerce/detail.html", context)


def signin(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                else:
                    return redirect('index')

    else:
        login_form = forms.LoginForm()

    context = {'login_form': login_form, 'next': request.GET.get('next')}
    return render(request, "ecommerce/login.html", context)


def signout(request):
    logout(request)
    return redirect('index')


@login_required
def product(request):
    if request.method == 'POST':
        product_form = forms.ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('index')

    else:
        product_form = forms.ProductForm()

    context = {
        'product_form': product_form
    }
    return render(request, "ecommerce/product.html", context)
