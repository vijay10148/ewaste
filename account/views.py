from django.http import response
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import avoid_wrapping
from .forms import AddProduct
from django.contrib.auth.models import Group
from account.models import UserDetail, UserProduct
from .forms import Createuserform
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user,allowed_users,admin_only
# Create your views here.
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    
    products=UserProduct.objects.all()

    
    totalproduct=products.count()
    
    # Returned=status.filter(status='Returned').count()
    # Pending=status.filter(status='Pending').count()
    # UnderProcess=status.filter(status='UnderProcess').count()
    context={'products':products}

    return render(request,'user-dashboard.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userhomepage(request):
    # status=inprocess.objects.all()
    log_user=request.user
    allproduct=UserProduct.objects.all()
    HP=allproduct.filter(producttype='HP').count()
    MACBOOK=allproduct.filter(producttype='MACBOOK').count()
    ASUS=allproduct.filter(producttype='ASUS').count()
    SAMSUNG=allproduct.filter(producttype='SAMSUNG').count()
    LENOVO=allproduct.filter(producttype='LENOVO').count()
    MINOTEBOOK=allproduct.filter(producttype='MI NOTEBOOK').count()
    ACER=allproduct.filter(producttype='ACER').count()
    DELL=allproduct.filter(producttype='DELL').count()
    products=UserProduct.objects.filter(user=log_user)
    # status=inprocess.objects.filter(user=log_user)
    # products=User.objects.get(username = request.user.username)
    # products=request.user.customer.order_set.all()
    # products=UserProduct.objects.filter(usernamekey=request.user.id)
    # products=request.user.UserProduct.order_set.all()

    # products=UserDetail.objects.filter(user=request.user).values()
    # products=UserProduct.objects.get(user=request.user).values()
    
    totalproduct=products.count()
    
    # Returned=status.filter(status='Returned').count()
    # Pending=status.filter(status='Pending').count()
    # UnderProcess=status.filter(status='UnderProcess').count()
    # context={'products':products,'UnderProcess':UnderProcess,'totalproduct':totalproduct,'status':status,'Returned':Returned,'Pending':Pending}

    # products=request.user. 
    context={'products':products,'totalproduct':totalproduct,'HP':HP,'MACBOOK':MACBOOK,'ASUS':ASUS,'SAMSUNG':SAMSUNG,'LENOVO':LENOVO,'MINOTEBOOK':MINOTEBOOK,'DELL':DELL,'ACER':ACER}
    return render(request,'userpage.html',context)    

# @login_required(login_url='login')
@unauthenticated_user
def loginpage(request):

    
    
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
               

        return render(request,'index.html')  
def logoutuser(request):
    logout(request)
    return redirect('startpage')      

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        form=Createuserform()
        if request.method=='POST':
            form=Createuserform(request.POST)
            if form.is_valid():
                user=form.save()
                user = form.cleaned_data.get('username')
                group=Group.objects.get(name='customer')
                
                user.groups.add(group)
                UserDetail.objects.create(
				user=user,
				name=user.username,
                
				)
            return redirect('login') 
            
    context={'form':form}

    
    return render(request,'register.html',context)    

def addproductuser1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddProduct(request.POST)
            if form.is_valid():
                thought = form.save(commit=False)
                thought.user = request.user
                thought.save()
                return HttpResponse('Hurray, saved!')
        else:
            form = AddProduct()
    else:
        return redirect('login')  
        
        

                
    return render(request,'adduserproduct.html',context={'form':form})

def purchased(request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        form=AddProduct()
        getdata=UserProduct.objects.filter(user=user)
        # statusdata=inprocess.filter(user=user)
        totalproduct=getdata.count()

    else:
        return redirect('login') 
    context={'form':form,'getdata':getdata,'totalproduct':totalproduct}     
    return render(request,'purchased.html',context)    


    

    


    


        
            
    
    


def userpage(request):


    return render(request,'userpage.html')

def adminpage(request):

    return render(request,'adminpage.html')

def startpage(request):
    return render(request,'startpage.html')

def skip(request):
     return render (request,'maintenance.html')   
