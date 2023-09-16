from django.http import HttpResponse,HttpResponseRedirect 
from django.shortcuts import render
from service.models import Contact
from service.models import Department
def indexPage(request):
    return render(request,'index.html')

def aboutPage(request):
    return render(request,"about.html")

def servicePage(request):
    return render(request,"service.html")

def departmentPage(request):
    # data = Department.objects.all()
    # print(data)
    data = Department.objects.all().values()
    # print(data)
  
    return render(request,"department.html",{'mydata':data})


def contactPage(request):
    # print($_POST)
    msg=''
    try:
          if request.method=="POST":
              f_name=request.POST['name']
              email=request.POST['email']
              subject=request.POST['subject']
              phone=request.POST['phone']
              message=request.POST['message']
              data=Contact(full_name=f_name,email_id=email,subject=subject,mob_num=phone,message=message)
              data.save()
              msg="Contact Data Send Succesfully !"
              
            #   print(f_name)
    except:
         pass    
    return render(request,'contact.html',{'message':msg})

def departmentSinglePage(request):
    return render(request,'department-single.html')

def doctor(request):
    return render(request,'doctor.html')

def doctor_single(request):
    return render(request,'doctor-single.html')

def appoinment(request):
    return render(request,'appoinment.html')


