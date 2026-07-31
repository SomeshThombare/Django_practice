from dapp.models import Employee
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee

# from PIL import pillow

def home(request):
    return render(request, "index.html")

# Create your views here.
def add_employees(request):
    if request.method == "POST":
        emp_name = request.POST.get('emp_name')
        emp_age = request.POST.get('emp_age')
        emp_salary = request.POST.get('emp_salary')
        emp_image = request.FILES.get('emp_image')
        obj = Employee(name = emp_name, age= emp_age, salary = emp_salary, image = emp_image)
        obj.save()
        return redirect  ('/list/')
    return render(request, 'add_employee.html')

def list_employees(request):
    data = Employee.objects.all()
    print(data)
    return render(request, 'employee_list.html', context = { 'data': data})

def update_employee(request, id):
    # obj = get_object_or_404(Employee,id = id)
    obj = Employee.objects.get(id = id)
    if request.method == "POST":
        obj.name = request.POST.get('emp_name')
        obj.age = int(request.POST.get('emp_age'))
        obj.salary = float(request.POST.get('emp_salary'))
        obj.save()
      
        return redirect('/list/')
    return render(request, 'update_employee.html', context = {'obj':obj})

def delete_employee(request, id):
    obj = Employee.objects.get(id = id)
    obj.delete()
    return redirect ('/list/')

def detailed_employee(request,id):
    obj = Employee.objects.get(id = id)
    return render(request, 'detailed.html',{'obj':obj})

def search_employee(request):
    data = None

    if request.method == "POST":
        search_name = request.POST.get('search-data')
        data = Employee.objects.filter(name__icontains = search_name)
        print(data)
    return render(request, 'employee_list.html', {'data':data})


    
