from django.urls import reverse

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
import json

def specific_bom_detail(request,bomname):
    bominfo_id = Bominfo.objects.get(bomname=bomname)
    qs = Bomlist.objects.values('material__code','material__description','material__partnumber','material__supplier__name','num','references').filter(bominfo=bominfo_id)
    '''
    print(qs,type(qs))
    total = qs.count()
    rows = []
    data = {'total': total, 'rows': rows, 'bomname':bomname}
    for q in qs:
        rows.append({
            'material__code': q.material__code,
            'material__description': q.material__description,
            'material__partnumber': q.material__partnumber,
            'material__supplier__name': q.material__supplier__name,
            'num': q.num,
            'references': q.references
        })
    return render(request,'specific_bom_detail.html',data,content_type='application/json')
    '''
    return render(request, 'specific_bom_detail.html', {'qs_list': qs})