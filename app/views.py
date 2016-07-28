from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from app.models import *
from django.views.decorators.http import require_GET
from django.core import serializers


@require_GET
def AllOrders(request):
    o = Order.objects.all()
    str = ""
    for object in o:
        str+= "{} : {} <br> {}<br>".format(object.client_id.name, object.date, object.products)

    oi = OrderItem.objects.all()
    #str = ""
    for object in oi:
        str += "{} : {} <br> {}<br>".format(object.product.name, object.order_id, object.total_cost)
    return HttpResponse(str)


# @require_GET
def IdOrder(request, o_id):
    try:
        o = Order.objects.filter(id=o_id)
    except:
        raise Http404()
    return JsonResponse(serializers.serialize('json', o), safe=False)
