from dapp.models import Employee
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee


# Create your views here.
def add_employees(request):
    if request.method == "POST":
        emp_name = request.POST.get('emp_name')
        emp_age = request.POST.get('emp_age')
        emp_salary = request.POST.get('emp_salary')
        obj = Employee(name = emp_name, age= emp_age, salary = emp_salary)
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