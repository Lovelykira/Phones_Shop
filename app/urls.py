from django.conf.urls import url, include
from django.contrib import admin
from app.views import ProductListView, ProductDetailView, ProductUpdateView, ProductCreateView, ProductDeleteView,OrderView

urlpatterns = [
    #url(r'^(?P<o_id>\d+)/$', IdOrder),
   # url(r'^$', AllOrders),
    url(r'^$', view=ProductListView.as_view(), name='product_list'),
    url(r'^(?P<pk>\d+)/$', view=ProductDetailView.as_view(), name='product_details'),
    url(r'^(?P<pk>\d+)/update/$', view=ProductUpdateView.as_view()),
    url(r'^create/$', view=ProductCreateView.as_view()),
    url(r'^(?P<pk>\d+)/delete/$', view=ProductDeleteView.as_view()),
    url(r'^(?P<pk>\d+)/order/$', view=OrderView.as_view()),
]