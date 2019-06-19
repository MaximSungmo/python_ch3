from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'helloworld/index.html')

# test 용 hello world 생성
def hello(request):
    return render(request, 'helloworld/helloworld.html')

def test_1(request):
    return render(request, 'helloworld/test_1.html')


