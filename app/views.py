from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'b':20,'c':80,'name':'mohana'}
    return render(request,'conditions.html',d)