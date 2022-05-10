from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models import *
import json
import datetime as dt
# Create your views here.

# Q1 function
def last48hoursData(request):
    date_from = dt.datetime.now() - dt.timedelta(days=2)
    queryset = Navigationrecord.objects.filter(datetime__gte=date_from).order_by('vehicle','datetime') 
    jsondata = json.dumps([x.serialize() for x in queryset], indent=2)
    return HttpResponse(jsondata, content_type="application/json")

# Q2 function

def binOperations(request):
    queryset = Bin.objects.select_related("op1","op2").all()
    dataList = []
    for query in queryset:
        dic = {}
        dic["name"] = query.name
        dic["latitude"] = query.latitude
        dic["longitude"] = query.longitude
        try:
            dic["operation1_collection_frequency"] = query.op1.collection_frequency
            dic["operation1_last_collection"] = query.op1.last_collection.strftime("%m.%d.%Y, %H:%M:%S")
        except Exception:
            dic["operation1_collection_frequency"] = ""
            dic["operation1_last_collection"] = ""
        try:
            dic["operation2_collection_frequency"] = query.op2.collection_frequency
            dic["operation2_last_collection"] = query.op2.last_collection.strftime("%m.%d.%Y, %H:%M:%S")
        except Exception:
            dic["operation2_collection_frequency"] = ""
            dic["operation2_last_collection"] = ""
        dataList.append(dic)

    jsondata = json.dumps(dataList, indent=2)
    return HttpResponse(jsondata, content_type="application/json")
    
