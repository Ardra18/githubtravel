# from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Person


# Create your views here.
def demo(request):
  obj=Place.objects.all()
  obj1=Person.objects.all()
  return render(request,"index.html",{'result':obj,'results':obj1})




# def operation(request):
#   x=int(request.GET['num1'])
#   y=int(request.GET['num2'])
#   res=x+y
#   res1=x-y
#   res2=x*y
#   res3=x/y
#   return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})
# def about(request):
#   return render(request,"about.html")
# def contact(request):
#   return render(request,"contact.html")
# def detail(request):
#   return HttpResponse("contact")
# def thanks(request):
#   return HttpResponse("thank you")
#
