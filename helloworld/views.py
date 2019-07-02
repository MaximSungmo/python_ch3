from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def index(request):
    return render(request, 'helloworld/index.html')

# test 용 hello world 생성
def hello(request):
    return render(request, 'helloworld/helloworld.html')

def test_1(request):
    return render(request, 'helloworld/test_1.html')

# pathvariable을 받을 때는 파라미터로 넣어주기
def hello2(request, id=0):
    return HttpResponse(f'id:{id}')


def hello3(request):
    jsonresult = {
        'result': 'success',
        'data': ['hello', 1, 2, True, ('a', 'b', 'c')]
    }
    return JsonResponse(jsonresult)


def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno = 0 if value["max_groupno"] is None else value["max_groupno"]

    return HttpResponse(f'max groupno:{value["max_groupno"]}')

def counter_add(request):
    c = Counter()
    c.groupno = 2
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 3
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 4
    c.depth = 1
    c.orderno = 1
    c.save()

    return HttpResponse('add')

def counter_update(request):
    # query set 예제
    # groupno = 1이고 orderno >=1 의
    # 게시물의 order_no를 1씩 증가
    # __gt, __lt, __gte, __lte
    Counter.objects.filter(groupno=2).filter(orderno__gte=1).update(depth=F('depth')+1)




    return HttpResponse('ok')

