from django.shortcuts import render

# Create your views here.
from crm.models import Employeemodel

from django.views.generic import View

class Createemployeeview(View):

    def get(self,request):

        return render(request,"add_employee.html")
    
    def post(self,request):

        print(request.POST)

        Employeemodel.objects.create(name = request.POST.get("username"),
                                     role = request.POST.get("userrole"),
                                     place = request.POST.get("userplace"),
                                     salary = request.POST.get("usersalary"))

        return render(request,"add_employee.html")
    
class EmployeeList(View):

    def get(self,request):

        data =Employeemodel.objects.all()

        return render(request,"employeelist.html",{"data":data})
    

class EmployeeUpdate(View):

    def get(self,request,**kwargs):

        update_id = kwargs.get("pk")

        emp_data = Employeemodel.objects.get(id=update_id)

        return render(request,"emp_update.html",{"emp_data":emp_data})
    
    def post(self,request,**kwargs):

        update_id = kwargs.get("pk")

        emp_data = Employeemodel.objects.get(id=update_id)

        print(request.POST)

        emp_data.name = request.POST.get("username") 

        emp_data.role = request.POST.get("userrole")

        emp_data.place = request.POST.get("userplace")

        emp_data.salary = request.POST.get("usersalary")

        emp_data.save()

        return render(request,"emp_update.html")
    

class Employeedelete(View):

     def get(self,request,**kwargs):

        delete_id = kwargs.get("pk")

        emp_data = Employeemodel.objects.get(id=delete_id)

        emp_data.delete()

        return render(request,"add_employee.html")
     

class EmployeeretriveView(View):

    def get(self,request,**kwargs):

        retrive_id = kwargs.get("pk")

        emp_data =  Employeemodel.objects.get(id= retrive_id)
        
        return render(request,"emp_details.html",{"emp_data":emp_data})



