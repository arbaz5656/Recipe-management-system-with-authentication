from django.shortcuts import render,redirect
from .models import recipehome
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def Home(request):
    if request.method == "POST":
        recipename=request.POST.get('recipename')
        recipedis=request.POST.get('recipedis')
        recipeimg=request.FILES.get('recipeimg')
        print(recipename)
        print(recipedis)
        print(recipeimg)
        # create operation
        varaible=recipehome.objects.create(recipename=recipename,recipedis=recipedis,recipeimg=recipeimg)

    # Search bar Logic
    queryset= recipehome.objects.all()
    if request.GET.get('Search'):
        queryset = queryset.filter(recipename__icontains = request.GET.get('Search'))

    data = { "rec" : queryset}
    return render(request,"home.html", data)


# @login_required(login_url="/login")
def update_res(request,id):
    query = recipehome.objects.get(id=id)
    if request.method == "POST":
        recipename=request.POST.get('recipename')
        recipedis=request.POST.get('recipedis')
        recipeimg=request.FILES.get('recipeimg')

        query.recipename=recipename
        query.recipedis=recipedis
        if recipeimg:
            query.recipeimg=recipeimg
        query.save()
        return redirect("/")
    context={"res":query}
    return render(request,"update.html",context)

def delete_res(request,id):
    # Delete Operation
    queryset=recipehome.objects.get(id=id).delete()
    return redirect("/")

from django.contrib.auth.models import User
from django.contrib import messages
def register_pg(request):
    if request.method == "POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")

        # user authentication check
        user=User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"Username is already taken,choose another username.")
            return redirect("/register")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Successfully")
        return redirect("/login")
    return render(request,"register.html")


from django.contrib.auth import authenticate,login
def login_pg(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request,"Invalid Username")
            return redirect('/login')
        p=authenticate(username=username,password=password)

        if p is None:
            messages.error(request,"Invalid Password")
            return redirect("/login")
        else:
            login(request,p)
            return redirect("/")

    return render(request,"login.html")


from django.contrib.auth import logout
def logout_pg(request):
    logout(request)
    return redirect('/login')
