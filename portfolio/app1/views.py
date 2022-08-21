from django.shortcuts import render,HttpResponse
from app1.models import Contact

# Create your views here.
def home(request):
    return render (request,'index.html')
def about(request):
    return HttpResponse("This is about page.")
def projects(request):
    return HttpResponse("This is projects page.")
def contact(request):
    if request.method=="POST":
       
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['number']
        concern=request.POST['concern']
        ins=Contact(name=name,email=email,phone=phone,concern=concern)
        ins.save()
        print("Info saved to db.")
    return HttpResponse("This is contact page.")
