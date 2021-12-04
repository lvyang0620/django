from django.core.paginator import Paginator

from django.urls import reverse
from django.views.generic import View
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models  import *

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

def index(request):
    #return HttpResponse('测试index请求，id={}'.format(id))
    return render(request,'index.html')

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