from django.urls import reverse

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
import json
from django.core.paginator import Paginator, EmptyPage


def specific_bom_detail(request,bomname):
    bominfo_id = Bominfo.objects.get(bomname=bomname)
    bominfo_bomlist_list = Bomlist.objects.values('material__code','material__description','material__partnumber','material__supplier__name','num','references').filter(bominfo=bominfo_id)

    paginator = Paginator(bominfo_bomlist_list, 10)  # 根据指定的每页列表大小进行分页
    try:
        current_page_num = int(request.GET.get('page', 1))
        page_bominfo_bomlist_list = paginator.page(current_page_num)  # 根据页数获取特定页的列表
        page_num = paginator.num_pages
    except EmptyPage:
        page_bominfo_bomlist_list = paginator.page(1)

    #  如果页数十分多时，换另外一种显示方式
    if paginator.num_pages > 11:  # 一般网页展示11页,左5页,右5页,加上当前页,共11页
        if current_page_num - 5 < 1:  # 如果前5页小于1时
            pageRange = range(1, 11)  # 页码的列表:范围是初始状态
        elif current_page_num + 5 > paginator.num_pages:  # 如果后5页大于总页数时
            # 页码的列表:范围是(当前页-5,总页数+1)。因为range顾头不顾尾,需要加1
            pageRange = range(current_page_num - 5, paginator.num_pages + 1)
        else:
            # 页码的列表:后5页正常时,页码范围是(当前页-5,当前页+6)。注意不是+5,因为range顾头不顾尾！
            pageRange = range(current_page_num - 5, current_page_num + 6)
    else:
        pageRange = paginator.page_range  # 页码的列表

    data = {
        'qs_list': page_bominfo_bomlist_list,
        'paginator': paginator,
        'current_page_num': current_page_num,
        'bomname': bomname,
        'pageRange':pageRange
    }

    return render(request, 'specific_bom_detail.html', data)