from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        return render(request, "index.html")

def index2(request):
    name = "yotam"
    return HttpResponse("<h1> Hello "+name+" </h1>")

def result(request):
    name = namecheck(request.POST['name'])
    fname = request.POST['fname']
    age = agecheck(request.POST['age'])
    return render(request, "result.html",{"x":name, "f":fname, "a":age})


def namecheck(name):
    if name=="yotam": 
        return name.upper()
    else:
        return name
        
def agecheck(age):
    Age = int(age)
    if 0<Age<=15:
        return "kid"
    else:
        if 15<Age<65:
            return "working age"
        else:
            return "old"

def details(request):
    return render(request, "details.html")
