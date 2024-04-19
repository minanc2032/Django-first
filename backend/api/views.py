import json
from urllib import request 
from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product 

#django models
@api_view(["GET"])
def api_home(requests, *args, **kwargs):
    """
    DRF API VIEW 
    """
    if request.method != "POST":
        return Response({"detail":"Get not allowed"}, status= 405)
    model_data = Product.objects.all().order_by("?").first()
    data ={}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','price','sale_price'])
    return Response(data)
        
       
        #print(data)
        #data = dict(data)
        #json_data_str = json.dumps(data)
    #return HttpResponse(json_data_str, headers={"content-type": "application/json"})
