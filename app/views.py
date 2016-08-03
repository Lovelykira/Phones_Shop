from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from app.models import *
from django.views.decorators.http import require_GET
from django.core import serializers
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Order, Client
from django.db.models import Q
from django.shortcuts import redirect

from app.forms import ProductForm


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'product/product_list.html'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        products = Product.objects.all()
        if q is not None:
            products = Product.objects.filter(Q(name__contains=q) )
        sort_by = self.request.GET.get('by')
        if sort_by is not None:
            sort_by = self.request.GET.get('in') + sort_by.lower()
            products = Product.objects.order_by(sort_by)
        return products


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect(self.get_success_url())


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self, **kwargs):
        return reverse_lazy('product_list')
