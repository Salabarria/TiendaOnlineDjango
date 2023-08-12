from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout ,authenticate

# Create your views here.

# function views of the app tasks
def home( request):
    myform = UserCreationForm()
    return  render(request,"home.html")
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
                login(request,usernew)
                return  redirect("tasks")
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
       
       
       
def tasks(request):
    data = " datos desde views.tasks()"
    return render(request,"tasks.html",{"midata":data})  


def signout(request):
    logout(request)
    return  redirect("home1") 

def signin(request):
    my_auth_form = AuthenticationForm()
    if request.method == "GET":
         return render(request,"signin.html",{"form_auth":my_auth_form})
    else:
        
         print(request.POST)
         user_valid = authenticate(request, username = request.POST["username"],password = request.POST["password"])
         if user_valid is None:
             return render(request,"signin.html",{
                 "form_auth":my_auth_form,
                 "error": "User and Password are incorrect"
                 
                 })
         else:
             login(request,user_valid)
             return redirect("tasks")
             
                
    
         


