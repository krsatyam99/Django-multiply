from unittest import result
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html',{})

def multiply(request):
    number1 = int( request.GET['num1'])
    number2 =  int(request.GET['num2'])
    result = number1*number2
    return render(request,'result.html',{'result':result})


    