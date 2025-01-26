from django.shortcuts import render

# Create your views here.

def homePage(request):
    context={}
    return render(request,'blog/index.html',context)

def blogpost(request,pk):
    pass