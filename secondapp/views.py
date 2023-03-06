from django.shortcuts import render

# Create your views here.
def loadfirstpage(request):
    return render(request,'first.html')

def loadsecondpage(request):
    return render(request,'second.html')