from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .services import (
    get_products,
    create_product,
    update_product,
    delete_product,
    get_product,
    delete_product_all
)
from .forms import ProductForm


class ProductsListView(LoginRequiredMixin, View):
    """Получает список всех продуктов"""

    def get(self, request: HttpRequest) -> HttpResponse:
        products = get_products()
        context = {
            "products": products
        }
        return render(request, 'products/product_list.html', context=context)

class ProductCreateView(LoginRequiredMixin, View):
    """Создает продукт"""

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": ProductForm()
        }
        return render(request, 'products/product_create.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ProductForm(request.POST)
        if form.is_valid():
            context = {
                "products": create_product(form=form)
            }
        return render(request, 'products/product_list.html', context=context)

class ProductUpdateView(LoginRequiredMixin, View):
    """Изменяет продукт"""

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        context = {
            "form": ProductForm()
        }
        return render(request, 'products/product_create.html', context=context)

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        form = ProductForm(request.POST)
        if form.is_valid():
            context = {
                "products": update_product(form, pk)
            }
        return render(request, 'products/product_list.html', context=context)


class ProductDeleteView(LoginRequiredMixin, View):
    """Удаляет продукт"""

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        context = {
            "products": delete_product(pk)
        }
        return render(request, 'products/product_list.html', context=context)


class ProductDetailView(LoginRequiredMixin, View):
    """Получает продукт по id"""

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        product = get_product(pk)
        context = {
            "products": product
        }
        return render(request, 'products/product_list.html', context=context)

class ProductsDeleteAllView(LoginRequiredMixin, View):
    """Удаляет все продукты"""

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "products": delete_product_all()
        }
        return render(request, 'products/product_list.html', context=context)
