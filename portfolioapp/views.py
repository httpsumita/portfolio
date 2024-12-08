from django.shortcuts import render
from .models import Project, Technology, PersonalInfo
# Create your views here.

def homePage(request):
    achievements=['Python','Prompt Engineering','AI integration','1000+ Linked', 'Community lead','2 Hackathons' ,'smart contracts','200+ DSA',]
    context={'achievements':achievements}
    return render(request,'portfolioapp/index.html',context)
