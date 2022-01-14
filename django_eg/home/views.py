from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_view, logout as logout_view
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
#from django.restframework

def index(request):
    return render(request, 'index.html')

def myfunctionabout(request):
    return render(request, 'about.html')

def myfunctioncontact(request):
    return render(request, 'contact.html')

def myfunctionlogin(request):
    if request.method == "POST":
        username=request.POST.get("username", None)
        password=request.POST.get("password", None)
        auth_user=authenticate(request, username=username, password=password)
        print(auth_user)
        if auth_user is not None:
            if auth_user.is_active:
                print("active user")
                login_view(request, auth_user)
                print("login success")
                return render(request,'success.html')
        else:

            return render(request, 'login.html')   
    return render(request, 'login.html')

def logout(request):
    return render(request, 'index.html')

     

def myfunctionregister(request):
    if request.method == "POST":
        name=request.POST.get("name", None)
        username=request.POST.get("username", None)
        email=request.POST.get("email", None)
        password=request.POST.get("password", None)
        User.objects.create_user(first_name=name, username= username, email= email, password=password)
        print(name,username, email, password)
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')
   

def myfunctionsuccess(request):
    args={'user': request.user}
    return render(request, 'success.html', args)

@login_required
def edit(request):
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        usr_instance = User.objects.get(email=email)
        usr_instance.first_name = first_name
        usr_instance.save()
        
       
        
        return render(request, 'edit.html')
    else:
        username = request.user.username
        instance = User.objects.all()
        return render(request, 'edit.html', {"users": instance})
    
def editnew(request):
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        usr_instance = User.objects.get(email=email)
        usr_instance.first_name = first_name
        usr_instance.save()
        return render(request, 'editnew.html')
    else:
        username = request.GET['username']
        instance = User.objects.get(username=username)
        return render(request, 'editnew.html', {"user": instance})
    
def delete(request):
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        usr_instance = User.objects.get(email=email)

        usr_instance.first_name = first_name
     
        usr_instance.delete()
        return render(request, 'delete.html')
    else:
        username = request.GET['username']
        instance = User.objects.get(username=username)
        return render(request, 'delete.html', {"user": instance})
