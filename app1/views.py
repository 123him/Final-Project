from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate
 
from app1.models import user_account,restaurant_account,tbl_accounts,food_menu,food_item
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def admin1(request):
    return render(request,'admin1.html')

def user1(request):
    data=request.session['username']
    return render(request,'user1.html',{'y':data})

def restur(request):
    return render(request,'restaurant.html')


def login(request):
    return render(request,'login.html')

def table(request):
    return render(request,'table.html')


def chef(request):
    return render(request,'chef.html')

def reservation(request):
    return render(request,'reservation.html')



def account(request):
    p1=User()
    p2=user_account()
    p3=tbl_accounts()
    p1.first_name=request.POST.get('fname')
    p1.last_name=request.POST.get('lname')
    p1.username=request.POST.get('user')
    password=request.POST.get('pwd')
    p1.set_password(password)
    p1.email=request.POST.get('mail')

    p2.first_name=request.POST.get('fname')
    p2.last_name=request.POST.get('lname')
    p2.gender=request.POST.get('gender')
    p2.phone=request.POST.get('ph')
    p2.email=request.POST.get('mail')
    p2.address=request.POST.get('adrs')                 
    p2.district=request.POST.get('district')
    p2.state=request.POST.get('state')
    p2.username=request.POST.get('user')
    photo=request.FILES['photo'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    p2.photo=uploaded_file_url

    p3.username=request.POST.get('user')
    p3.firstname=request.POST.get('fname')
    p3.account_type="user"
    
    p1.save()
    p2.save()
    p3.save()
    return redirect('/login')

def login1(request):
    username=request.POST.get('user')
    password=request.POST.get('pwd')
    data=authenticate(username=username,password=password)
    request.session['username']=username
    if data is not None and data.is_superuser==1:
        return redirect('/admin1/')
    elif data is not None and data.is_superuser==0:
        a=tbl_accounts.objects.get(username=data.username)
        if a.account_type=="user":
            return redirect('/userHome/')
        elif a.account_type=="rest_admin":
            return redirect('/restaurentHome/')
    else:
        return HttpResponse('invalid_user')
def restaurentHome(request):
    a=request.session['username']
    return render(request,'restaurant.html',{'x':a})
def userHome(request):
    a=request.session['username']
    return render(request,'user1.html',{'x':a})


def account2(request):
    p1=User()
    p2=restaurant_account()
    p3=tbl_accounts()
    p1.first_name=request.POST.get('fname')
    p1.last_name=request.POST.get('lname')
    p1.username=request.POST.get('user')
    password=request.POST.get('pwd')
    p1.set_password(password)
    p1.email=request.POST.get('mail')

    p2.first_name=request.POST.get('fname')
    p2.last_name=request.POST.get('lname')
    p2.restaurant_name=request.POST.get('restaurant_name')
    p2.phone=request.POST.get('ph')
    p2.email=request.POST.get('mail')
    p2.location=request.POST.get('location')                 
    p2.type_of_restaurant=request.POST.get('type')
    p2.no_of_staff=request.POST.get('staffs')
    p2.username=request.POST.get('user')
    p2.authorised_person=request.POST.get('authorised')
    photo=request.FILES['photo'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    p2.photo=uploaded_file_url
    p2.status=request.POST.get('status')

    p3.username=request.POST.get('user')
    p3.firstname=request.POST.get('fname')
    p3.account_type="rest_admin"
    
    
    p1.save()
    p2.save()
    p3.save()
    return redirect('/login')

def create_restaurant(request):
    return render(request,'create_restaurant.html')

def addFood(request):
    a=request.session['username']
    return render(request,'addfood.html',{'x':a})

def foodmenu1(request):
    p1=food_menu()

    p1.restaurant_name=request.POST.get('restaurant')
    p1.menu_name=request.POST.get('menu')
    p1.type=request.POST.get('type')
    p1.cruises=request.POST.get('cruises')
    p1.orgin=request.POST.get('orgin')
    photo=request.FILES['photo']
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    p1.photo=uploaded_file_url
    p1.save()
    return redirect('/restaurentHome/')

def items(request):
    data1=request.session['username']
    data2=food_menu.objects.filter(restaurant_name=data1)
    return render(request,'addFoodItem.html',{'x':data1,'y':data2})

def item1(request):
    p1=food_item()

    p1.restaurant_name=request.POST.get('restaurant')
    p1.menu_name=request.POST.get('menu')
    p1.menu_item_name=request.POST.get('item')
    p1.quantity=request.POST.get('qty')
    p1.price=request.POST.get('rs')
    p1.type=request.POST.get('type')
    p1.cooking_time=request.POST.get('tym')
    p1.status=request.POST.get('status')
    photo=request.FILES['photo']
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    p1.photo=uploaded_file_url
    p1.save()
    return redirect('/restaurentHome/')

def viewRestaurant(request):
    data=restaurant_account.objects.all()
    return render(request,'view_restaurant.html',{'x':data})

def viewFooditems(request):
    return render(request,'view_fooditems.html')

def admin_viewRestaurant(request):
    a=restaurant_account.objects.all()
    return render(request,'admin_viewRestaurant.html',{'x':a})

def admin_updateRestaurant(request,id):
    datas=restaurant_account.objects.get(id=id)
    return render(request,'admin_updateRestaurant.html',{'y':datas})

def update_restaurantAdmin1(request,id):
    p2=restaurant_account.objects.get(id=id)
    try:
        p2.first_name=request.POST.get('fname')
        p2.last_name=request.POST.get('lname')
        p2.restaurant_name=request.POST.get('restaurant_name')
        p2.phone=request.POST.get('ph')
        p2.email=request.POST.get('mail')
        p2.location=request.POST.get('location')                 
        p2.type_of_restaurant=request.POST.get('type')
        p2.no_of_staff=request.POST.get('staffs')
        p2.username=request.POST.get('user')
        p2.authorised_person=request.POST.get('authorised')
        photo=request.FILES['photo'] 
        fs= FileSystemStorage()
        filename=fs.save(photo.name,photo) 
        uploaded_file_url=fs.url(filename)
        p2.photo=uploaded_file_url
        p2.status=request.POST.get('status')
        
        p2.save()
    except:
        p2.first_name=request.POST.get('fname')
        p2.last_name=request.POST.get('lname')
        p2.restaurant_name=request.POST.get('restaurant_name')
        p2.phone=request.POST.get('ph')
        p2.email=request.POST.get('mail')
        p2.location=request.POST.get('location')                 
        p2.type_of_restaurant=request.POST.get('type')
        p2.no_of_staff=request.POST.get('staffs')
        p2.username=request.POST.get('user')
        p2.authorised_person=request.POST.get('authorised')
        p2.status=request.POST.get('status')

        p2.save()
        return redirect('/admin_viewRestaurant/')

def admin_deleteRestaurant(request,id):
    datas1=restaurant_account.objects.get(id=id)
    datas1.delete()
    return redirect('/admin_viewRestaurant/')