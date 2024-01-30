from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html',{'name':"May god bless this course"})


#getting two numbers from user and displaying the result in result.html
def add(request):
    val1= request.POST['num1']
    val2=request.POST['num2']
    res=int(val1)+int(val2)
    return render(request,'result.html', {'result': res})    

# Create your views here.
