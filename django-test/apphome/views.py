import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Customers

# Create your views here.
def index(request):
	latest_customer_list = Customers.objects.order_by("cid")[:2]
	output = ", ".join([str(c.rid) for c in latest_customer_list])
	#customer = Customers.objects.get(cid=1)
	#output = customer.rid
	return HttpResponse(output)
	#return HttpResponse("Hello, World!")

def detail(request, cid):
	customer = Customers.objects.get(cid = 1)
	output = customer.rid
	return HttpResponse(output)
	#return HttpResponse("You're looking at customer %d." % cid)



def get_post(request):
    if request.method == 'GET':
        customer_id = request.GET['cid']
	#customer = Customers.objects.get(cid=1)
        data = {
            'data': customer_id,
        }
        return render(request, 'apphome/parameter.html', data)
	#return JsonResponse({"message":customer_information}, status=200)
	#return JsonResponse({"message":data}, status=200)


class CustomerView(View):
    def get(self, request):
        customer_id = request.GET.get('cid', None)
        customer = Customers.objects.get(cid=customer_id)
        customer_information = {
            'Customer_id': customer.cid,
	    'Restaurant_id' : customer.rid,
        }
        return JsonResponse({"message":customer_information}, status=200)
