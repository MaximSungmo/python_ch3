from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
    emaillist = Emaillist.objects.all().order_by('-id')
    data = { 'emalilist': emaillist }
    #객체를 담아서 view로 보내는 방법은 객체를 dict로 담아서 return 시 넘겨주면 된다.
    print(data)
    return render(request, 'emaillist/index.html', data)

def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    # 모델을 호출해서 넣어주기
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']
    emaillist.save()
    # 만약 Http로 바로 응답하고 싶으면 아래와 같이.
    # return HttpResponse(f'{firstname}:{lastname}:{email}')
    return HttpResponseRedirect('/emaillist')






