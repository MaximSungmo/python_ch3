from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

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



