from django.shortcuts import render
from Products.models import Products
from django.shortcuts import redirect
from .models import Products


# Create your views here.
def home(request):
    return render(request,'index.html')

def AddProducts(request):
    if request.method == "POST":
        p_name = request.POST.get('p_name')
        p_brand = request.POST.get('p_brand')
        p_price = int(request.POST.get('p_price'))
        p_quantity = int(request.POST.get('p_quantity'))
        p_exp_date = request.POST.get('p_exp_date') 
        
        obj = Products(name = p_name, brand = p_brand,  price = p_price, quantity = p_quantity, exp_date = p_exp_date)

        obj.save()
        return redirect('/list/')
    return render(request, 'add_products.html')

def ListProducts(request):
    data = Products.objects.all()
    print(data)
    return render(request,'product_list.html', context= {'data': data})

def update(request, id):
    obj = Products.objects.get(id = id)
    if request.method == "POST":
        obj.name = request.POST.get('p_name')
        obj.brand = request.POST.get('p_brand')
        obj.price = float(request.POST.get('p_price'))
        obj.quantity = int(request.POST.get('p_quantity'))
        obj.exp_date = request.POST.get('p_exp_date')

        obj.save()
      
        return redirect('/list/')
    return render(request, 'update_products.html', context = {'obj':obj})


def Delete(request,id):
    obj = Products.objects.get(id=id)
    obj.delete()
    return redirect('/list/')