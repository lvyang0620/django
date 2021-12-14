from django.core.paginator import Paginator

from django.urls import reverse
from django.views.generic import View
from django.views.generic.list import ListView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from .models  import *
from django.http import JsonResponse
from django.db.models import F


# 用Listview实现Supplier列表显示
class SupplierListView(ListView):
    #查询的模型
    model = Supplier
    #每页显示5条
    paginate_by = 5

# 用Listview实现Supplier列表显示
class CategoryListView(ListView):
    #查询的模型
    model = Category
    #每页显示5条
    paginate_by = 5

# 用Listview实现Project列表显示
class ProjectListView(ListView):
    #查询的模型
    model = Project
    #每页显示5条
    paginate_by = 5

# 用Listview实现Material列表显示
class MaterialtListView(ListView):
    #查询的模型
    model = Material
    #每页显示5条
    paginate_by = 10

# 用Listview实现Bominfo列表显示
class BominfoListView(ListView):
    #查询的模型
    model = Bominfo
    #每页显示5条
    paginate_by = 10

# 用Listview实现Bomlist列表显示
class BomlistListView(ListView):
    #查询的模型
    model = Bomlist
    #每页显示5条
    paginate_by = 10

# 从Bominfo查询bomlist明细
class BominfoToBomlistListView(ListView):
    #查询的模型
    #model = Bomlist
    template_name = 'bom/bominfotobomlist_list.html'
    def get_queryset(self):
        #qs = super().get_queryset()  # 调用父类方法
        bomname = self.request.GET.get('bomname',None)
        qs = Bomlist.objects.values('material__code','material__description','material__partnumber','material__supplier__name','num','references').filter(bominfo__bomname=bomname)
        return qs
    def get_context_data(self, **kwargs):
        bomname = self.request.GET.get('bomname')
        bominfo = Bominfo.objects.filter(bomname=bomname)
        context = super().get_context_data(**kwargs)
        context.update({'bomname': bomname,'hw_version':bominfo.first().hw_version,'description':bominfo.first().description,'project':bominfo.first().project})
        return context
    paginate_by = 500

# 用Listview实现# 用Listview实现Ecn列表显示列表显示
class EcnListView(ListView):
    #查询的模型
    model = Ecn
    paginate_by = 10

#首页
def index(request):
    project = Project.objects.all()
    supplier = Supplier.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',locals())

def project(request):
    project = Project.objects.all()
    paginator = Paginator(project, 10)  # 根据指定的每页列表大小进行分页
    try:
        current_page_num = int(request.GET.get('page', 1))  # 根据url获取当前页，没有时取1
        project = paginator.page(current_page_num)  # 根据页数获取特定页的列表
        page_num = paginator.num_pages
        page_range = paginator.page_range
    except EmptyPage:
        project = paginator.page(1)
    return render(request,'page_project.html',locals())

def category(request):
    # project = Project.objects.all()
    # supplier = Supplier.objects.all()
    category = Category.objects.all()
    paginator = Paginator(category, 10)  # 根据指定的每页列表大小进行分页
    try:
        current_page_num = int(request.GET.get('page', 1))  # 根据url获取当前页，没有时取1
        category = paginator.page(current_page_num)  # 根据页数获取特定页的列表
        page_num = paginator.num_pages
        page_range = paginator.page_range
    except EmptyPage:
        category = paginator.page(1)
    return render(request,'page_category.html',locals())

def supplier(request):
    # project = Project.objects.all()
    supplier = Supplier.objects.all()
    paginator = Paginator(supplier, 10)  # 根据指定的每页列表大小进行分页
    try:
        current_page_num = int(request.GET.get('page', 1))  # 根据url获取当前页，没有时取1
        supplier = paginator.page(current_page_num)  # 根据页数获取特定页的列表
        page_num = paginator.num_pages
        page_range = paginator.page_range
    except EmptyPage:
        supplier = paginator.page(1)
    return render(request,'page_supplier.html',locals())

def material(request):
    # project = Project.objects.all()
    # supplier = Supplier.objects.all()
    # category = Category.objects.all()
    material = Material.objects.all()
    paginator = Paginator(material, 10)  # 根据指定的每页列表大小进行分页
    try:
        current_page_num = int(request.GET.get('page', 1))  # 根据url获取当前页，没有时取1
        material = paginator.page(current_page_num)  # 根据页数获取特定页的列表
        page_num = paginator.num_pages
        page_range = paginator.page_range
    except EmptyPage:
        material = paginator.page(1)
    return render(request,'page_material.html',locals())

def ecn(request):
    # project = Project.objects.all()
    # supplier = Supplier.objects.all()
    # category = Category.objects.all()
    # material = Material.objects.all()
    ecn = Ecn.objects.all()
    paginator = Paginator(ecn, 10)  # 根据指定的每页列表大小进行分页
    try:
        current_page_num = int(request.GET.get('page', 1))      # 根据url获取当前页，没有时取1
        ecn = paginator.page(current_page_num)  # 根据页数获取特定页的列表
        page_num = paginator.num_pages
        page_range = paginator.page_range
    except EmptyPage:
        ecn = paginator.page(1)
    return render(request,'page_ecn.html',locals())

def bominfo(request):
    project = Project.objects.all()
    # print(project)
    # supplier = Supplier.objects.all()
    # category = Category.objects.all()
    # material = Material.objects.all()
    # ecn = Ecn.objects.all()
    bominfo = Bominfo.objects.all().order_by('id')
    paginator = Paginator(bominfo, 500)  # 分页先设为500，咱不分页，后续完善
    try:
        current_page_num = int(request.GET.get('page', 1))      # 根据url获取当前页，没有时取1
        bominfo = paginator.page(current_page_num)  # 根据页数获取特定页的列表
        page_num = paginator.num_pages
        page_range = paginator.page_range
    except EmptyPage:
        bominfo = paginator.page(1)
    return render(request,'page_bominfo.html',locals())

def bomdetail(request,bomname):
    # project = Project.objects.all()
    # supplier = Supplier.objects.all()
    # category = Category.objects.all()
    # material = Material.objects.all()
    # ecn = Ecn.objects.all()
    bominfo = Bominfo.objects.filter(bomname=bomname)
    bomname = bomname
    hw_version = bominfo.first().hw_version
    description = bominfo.first().description
    project = bominfo.first().project
    bomdetail = Bomlist.objects.filter(bominfo__bomname=bomname)
    paginator = Paginator(bomdetail, 10)  # 根据指定的每页列表大小进行分页
    try:
        current_page_num = int(request.GET.get('page', 1))  # 根据url获取当前页，没有时取1
        bomdetail = paginator.page(current_page_num)  # 根据页数获取特定页的列表
        page_num = paginator.num_pages
        page_range = paginator.page_range
    except EmptyPage:
        bomdetail = paginator.page(1)
    return render(request,'page_bomdetail.html',locals())

#测试重定向
def test_reverse(request,id):
    return HttpResponse('测试重定向，id={}'.format(id))
#重定向
def test(request,id):
    #使用命名空间
    result = reverse('bom:test_reverse',args=(id,))
    return HttpResponseRedirect(result)
#加入前台测试
def test02(request):
    #第三个参数是上下文环境
    return render(request,'test_reverse.html')