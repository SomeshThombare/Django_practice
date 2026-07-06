from django.shortcuts import render

# Create your views here.
def homePage(request):
    data = {
        'title' : 'HomePage',
        'bdata' : 'Welcome to Homepage with dict',
        'course':['java','python','c++'],
        'numbers':[10,20,30,40,50],
        'stud_details':[
            {'name':'sam','ph_no':123654789},
            {'name':'somesh','ph_no':87896541123}
        ]
    }
    
    return render(request, 'homepage.html',data)

def aboutUs(request):
    return render(request, 'aboutus.html')

def landingPage(request):
    return render(request,'index.html')