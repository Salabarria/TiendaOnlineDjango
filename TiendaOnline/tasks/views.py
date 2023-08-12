from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.

# function views of the app tasks
def helloworld( request):
    myform = UserCreationForm()
    return HttpResponse("hello world")
    #return render(request,'signup.html',{'form':myform})

def signup(request):
    myform = UserCreationForm() 
    if request.method == "GET":
        print(request.GET) 
               
        return render(request, "signup.html",{"form":myform})
    if request.method == "POST":
        print(request.POST) 
         
        if request.POST['password1'] == request.POST['password2']:
            # password susscefull and register user
            try:
                usernew =User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                usernew.save()
                return  HttpResponse("User created successfully")
            except:
                return render(request, "signup.html",{
                    "form":myform,"error":
                    "username alredy exists"
                    })
        
        else:
            # password wrognt
        
            # return render(request, "signup.html",{"form":myform})  
            return render(request, "signup.html",{
                    "form":myform,
                    "error":
                    "passwordd do not match"
                    })
       
    


