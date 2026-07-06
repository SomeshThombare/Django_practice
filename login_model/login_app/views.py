from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def loginPage(request):
    return render(request,'login.html')

def message(request):
    return render(request,'message.html')


def notification(request): 
    return render(request, 'notification.html') 

def profile(request):
    return render(request,'profile.html')

def form(request):
    print("request.method:",request.method)
    if request.method == 'GET':
        print("GET:",request.GET)
        return render(request,'form.html')
    elif request.method == 'POST':
        print("POST:",request.POST)
        num1 = int(request.POST.get('f_num'))
        num2 = int(request.POST.get('l_num'))
        res =  num1 + num2
        return HttpResponse(res)

    
       
def mul_view(request):
    print(request.GET)
    a = int(request.GET.get('p'))
    b = int(request.GET.get('q'))
    c = a + b
    return HttpResponse(c)