import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.db.models import Max
from datetime import datetime
from django.utils import timezone
from datetime import timedelta

from .models import Customers
from .models import Restaurants
from .models import Inference

# Create your views here.
def index(request):
	latest_customer_list = Customers.objects.order_by("cid")[:2]
	output = ", ".join([str(c.rid) for c in latest_customer_list])
	#customer = Customers.objects.get(cid=1)
	#output = customer.rid
	return HttpResponse(output)
	#return HttpResponse("Hello, World!")

def get_post_wait(request):
     # [WAIT] GET request
     if request.method == 'GET':
        wait_team = Inference.objects.filter(enter=False).count()
        max_time = Inference.objects.all().aggregate(max_time = Max('estimated_time'))
        wait_time = max_time['max_time']

        data = {
            'num_team': wait_team,
            'wait_time': wait_time,
        }
        return JsonResponse(data, status=200)
     
     # [WAIT] POST request
     else:
        data = json.loads(request.body)
        people = data["people"]
        kakao = data["kakao"]
        infer_time = data["infer_time"]
        Inference.objects.create(num_guest=people, phone_number=kakao, estimated_time=infer_time)
        return JsonResponse({'message': 'Data saved successfully.'})
         

def get_post_order(request):
    # [ORDER] GET request
     if request.method == 'GET':
        customer_id = request.GET['cid']
        try:
            customer = Customers.objects.get(cid=customer_id)
            menu = customer.menu
            return JsonResponse({'menu': menu}, status=200)
        except Customers.DoesNotExist:
            return JsonResponse({'error': 'Customer not found.'})
    # [ORDER] POST request
     else:
        data = json.loads(request.body)
        menu = data["menu"]
        time = datetime.now()
        interval = timedelta(days=0, hours=0, minutes=30)
        Customers.objects.create(menu=menu, enter_time = time, out_time = time, Total_time = interval)
        return JsonResponse({'message': 'Data saved successfully.'})

class CustomerView(View):
    def get(self, request):
        customer_id = request.GET.get('cid', None)
        customer = Customers.objects.get(cid=customer_id)
        customer_information = {
            'Customer_id': customer.cid,
	    'Restaurant_id' : customer.rid,
        }
        return JsonResponse({"message":customer_information}, status=200)
