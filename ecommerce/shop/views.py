from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import Category,Products
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def category(request):
    item=Category.objects.all()
    return render(request,'category.html',{'item':item})

def products(request,m):
    pro=Category.objects.get(id=m)
    item=Products.objects.filter(category=pro)

    return render(request,'products.html',{'product':pro,'item':item})

def product_details(request,i):
    pro=Products.objects.get(id=i)
    return render(request,'productdetails.html',{'product':pro})



def register(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        fn = request.POST['fn']
        ln = request.POST['ln']
        if (cp==p):
            user = User.objects.create_user(username=u,password=p,first_name=fn,last_name=ln,email=e)
            user.save()
            return redirect('shop:user_login')
        else:
            return HttpResponse('any mistake are done')
    return render(request, 'register.html')

def user_login(request):
    if (request.method == 'POST'):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('shop:category')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request, 'login.html')