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
    #查询返回结果集，优先级最好，设置以后model失效
    #queryset =
    #每页显示5条
    paginate_by = 5

# 用Listview实现Supplier列表显示
class CategoryListView(ListView):
    #查询的模型
    model = Category
    #查询返回结果集，优先级最好，设置以后model失效
    #queryset =
    #每页显示5条
    paginate_by = 5

# 用Listview实现Project列表显示
class ProjectListView(ListView):
    #查询的模型
    model = Project
    #查询返回结果集，优先级最好，设置以后model失效
    #queryset =
    #每页显示5条
    paginate_by = 5

# 用Listview实现Material列表显示
class MaterialtListView(ListView):
    #查询的模型
    model = Material
    #查询返回结果集，优先级最好，设置以后model失效
    #queryset =
    #每页显示5条
    paginate_by = 10

# 用Listview实现Bominfo列表显示
class BominfoListView(ListView):
    #查询的模型
    model = Bominfo
    #查询返回结果集，优先级最好，设置以后model失效
    #queryset =
    #每页显示5条
    paginate_by = 10

# 用Listview实现Bomlist列表显示
class BomlistListView(ListView):
    #查询的模型
    model = Bomlist
    #查询返回结果集，优先级最好，设置以后model失效
    #queryset =
    #每页显示5条
    paginate_by = 10

# 用Listview实现# 用Listview实现Ecn列表显示列表显示
class EcnListView(ListView):
    #查询的模型
    model = Ecn
    #查询返回结果集，优先级最好，设置以后model失效
    #queryset =
    #每页显示5条
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