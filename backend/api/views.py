import json
from urllib import request 
from django.forms.models import model_to_dict
#from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product 
from products.serializers import ProductSerializer

#django models
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW 
    """
    #data = request.data 
    serializer = ProductSerializer(data=request.data )
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)

    #if request.method != "POST":
        #return Response({"detail":"Get not allowed"}, status= 405)
   # instance = Product.objects.all().order_by("?").first()
    #data ={}
    #if instance:
        #data = model_to_dict(instance, fields=['id','title','price','sale_price'])
        #data = ProductSerializer(instance).data   
        #print(data)
        #data = dict(data)
        #json_data_str = json.dumps(data)
    #return HttpResponse(json_data_str, headers={"content-type": "application/json"})

