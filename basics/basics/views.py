from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html',{'name':'Navin'});

def add(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res=val1+val2
    res1=val1-val2
    res2=val1*val2

    return render(request,'result.html',{'result':res,'result1':res1,
                  'result2':res2})


