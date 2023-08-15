from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout ,authenticate
from tasks.forms import TaskForm
from tasks.models import Task

# Create your views here.

# function views of the app tasks
########################################################
def home( request):
    myform = UserCreationForm()
    return  render(request,"home.html")
    #return render(request,'signup.html',{'form':myform})
#####################################################################
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
       
       
#############################################################       
def tasks(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.filter(user = request.user)
    print(tasks)
    data = " datos desde views.tasks()"
    return render(request,"tasks.html",{"mis_tareas":tasks})  
###########################################################
def create_task(request):
    my_form_task = TaskForm()
    if request.method == "GET":
        # print(request.GET)
        return render(request,"create_task.html",{
            "form_task": my_form_task
            })
        #
    else:
        try: 
            form_temp = TaskForm(request.POST)
            print(form_temp)
            print(request.POST)
            new_task = form_temp.save(commit=False)
            new_task.user = request.user
            new_task.save()
            # return render(request,"create_task.html",{
            # "form_task": my_form_task  })
            return redirect("tasks")
           
        except:
            return render(request,"create_task.html",{
            "form_task": my_form_task,
            "error":"Please provide valida data"
            
            })
            
################################################################
def signout(request):
    logout(request)
    return  redirect("home1") 

#########################################################
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
############################################################v             
                
def task_detail(request,task_id):
    
    task = Task.objects.get(id = task_id)
    
    print(task.title)
    return render(request,"task_detail.html",{
                 "title":task.title,
                                  
                 }) 
         

############################################################v  
###################
