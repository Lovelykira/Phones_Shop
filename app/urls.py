from django.conf.urls import url, include
from django.contrib import admin
from app.views import AllOrders, IdOrder

urlpatterns = [
    url(r'^(?P<o_id>\d+)/$', IdOrder),
    url(r'^$', AllOrders),
]