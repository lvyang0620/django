from django.urls import reverse

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *

def specific_bom_detail(request,bomname):
    bominfo_id = Bominfo.objects.get(bomname=bomname)
    qs = Bomlist.objects.values('material__code','material__description','material__partnumber','material__supplier__name','num','references').filter(bominfo=bominfo_id)
    print(qs,type(qs))
    #for q in qs:
        #print(q.material,q.num,q.references)
    #return HttpResponse(qs)
    return render(request,'specific_bom_detail.html',{'qs_list':qs})