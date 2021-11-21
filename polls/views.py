from django.shortcuts import render
from django.http import HttpResponse, Http404
from polls.models import Question, Choise

# Create your views here.
#首页，展示所有问题
def index1(request):
    qs = Question.objects.all()
    #使用列表生成式返回页面结果
    #output = ','.join([q.question_text for q in qs])
    output='''
        <ul>
            <li><a href="#">{}</a></li>
            <li><a href="#">{}</a></li>
            <li><a href="#">{}</a></li>
        </ul>
    '''.format(qs[0].question_text,qs[1].question_text,qs[2].question_text)
    return HttpResponse(output)

def index(request):
    qs = Question.objects.all()
    #使用列表生成式返回页面结果
    context = {'qs':qs}
    return render(request,'index.html',context)

#问题详情页
def detail(request,question_id):
    try:
        q = Question.objects.get(pk=question_id)
        #准备context
        context = {'detail':q}
        return render(request,'detail.html',context)
    except Question.DoesNotExist as e:
        raise Http404('该数据不存在')
#问题结果页
def result(request,question_id):
    q = Question.objects.get(pk=question_id)
    return HttpResponse("所要查看的[%s]结果页" %q.question_text)
#投票页
def votes(request,question_id):
    q = Question.objects.get(pk=question_id)
    return HttpResponse("所要查看的[%s]投票页" % q.question_text)