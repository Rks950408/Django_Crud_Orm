from django.shortcuts import render
from crud_app.models import tbl_employee

def create(request):
    if request.method == "POST":
        print(request.POST, "================post request")
        e_name = request.POST.get('emp_name')  
        e_email = request.POST.get('emp_email')  
        e_mobile = request.POST.get('emp_mobile') 

        qs = tbl_employee.objects.create(name=e_name, email=e_email, mobile=e_mobile)
        print(qs.id, "print id here")

        if qs:
            return render(request, "retrive.html")  
    else:
        return render(request, "create_emp.html")
