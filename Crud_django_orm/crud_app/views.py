from django.shortcuts import render,redirect
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
            return redirect('retrieve')  
    else:
        return render(request, "create_emp.html")

def reterive(request):
    qs=tbl_employee.objects.all()
    context={
       'emp_data':qs
    }
    return render(request, "retrive.html",context)

def delete_emp(request, emp_id):
    try:
        # Try to retrieve and delete the employee object
        employee = tbl_employee.objects.get(id=emp_id)
        employee.delete()
        return redirect('retrieve')  # Redirect to the retrieve page after deletion
    except tbl_employee.DoesNotExist:
        # Handle the case where the employee doesn't exist
        return render(request, 'error.html', {'message': 'Employee not found'})


def update_emp(request, emp_id):
    if request.method == 'POST':
        print(request.POST, '----------------------\n')
        e_name = request.POST.get('emp_name')
        e_email = request.POST.get('emp_email')
        e_mobile = request.POST.get('emp_mobile')
        print(e_mobile)

        qs = tbl_employee.objects.filter(id=emp_id).update(
            name=e_name, 
            email=e_email, 
            mobile=e_mobile
            )
        
        if qs:
            return redirect('retrieve')   # Redirect to retrieve page on success

    else:
        print(emp_id, '============= update emp_id ==============\n')
        qs = tbl_employee.objects.get(id=emp_id)
        return render(request, 'update.html', {'emp_update_data': qs})