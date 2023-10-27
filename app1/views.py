from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate
 
from app1.models import user_account,restaurant_account,tbl_accounts,food_menu,food_item,offer,tbl_cart,tbl_order
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
    data7=user_account.objects.get(username=data)
    return render(request,'user1.html')



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
    a1=user_account.objects.get(username=a)
    return render(request,'user1.html',{'x':a1})


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
    p2.restaurant_name=request.POST.get('restaurant')
    p2.phone=request.POST.get('ph')
    p2.email=request.POST.get('mail')
    p2.location=request.POST.get('location')                 
    p2.type_of_restaurant=request.POST.get('type')
    p2.no_of_staff=request.POST.get('staff')
    p2.username=request.POST.get('user')
    p2.authorised_person=request.POST.get('authorised')
    photo=request.FILES['img']
    fs=FileSystemStorage()
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
    return redirect('/admin1/')

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

def viewFooditems(request,restaurant_name):
    data6=food_item.objects.filter(restaurant_name=restaurant_name)

    return render(request,'view_fooditems.html',{'x':data6})

def admin_viewRestaurant(request):
    b=restaurant_account.objects.all()
    return render(request,'admin_viewRestaurant.html',{'x':b})

def admin_updateRestaurant(request,id):
    datas=restaurant_account.objects.get(id=id)
    return render(request,'admin_updateRestaurant.html',{'y':datas})

def update_restaurantaadmin(request,id):
    p2=restaurant_account.objects.get(id=id)
    try:
        p2.first_name=request.POST.get('fname')
        p2.last_name=request.POST.get('lname')
        p2.restaurant_name=request.POST.get('restaurant')
        p2.phone=request.POST.get('ph')
        p2.email=request.POST.get('mail')
        p2.location=request.POST.get('location')                 
        p2.type_of_restaurant=request.POST.get('type')
        p2.no_of_staff=request.POST.get('staff')
        p2.authorised_person=request.POST.get('authorised')
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        photo=fs.save(photo.name,photo)
        image1 =fs.url(photo)
        p2.photo = image1
        p2.status=request.POST.get('status')
        p2.save()
    except:
        p2.first_name=request.POST.get('fname')
        p2.last_name=request.POST.get('lname')
        p2.restaurant_name=request.POST.get('restaurant')
        p2.phone=request.POST.get('ph')
        p2.email=request.POST.get('mail')
        p2.location=request.POST.get('location')                 
        p2.type_of_restaurant=request.POST.get('type')
        p2.no_of_staff=request.POST.get('staff')
        p2.authorised_person=request.POST.get('authorised')
        p2.save()
    return redirect('adview_restaurant/')

def viewadmin_restaurant(request):
    d1=restaurant_account.objects.all()
    return render(request,'viewadmin_restaurant.html',{'x':d1})

def adminupdate_restaurant(request,id):
    d=restaurant_account.objects.get(id=id)
    return render(request,'adminupdate_restaurant.html',{'y':d})

def update1(request,id):
    p2=restaurant_account.objects.get(id=id)
    try:
        p2.first_name=request.POST.get('fname')
        p2.last_name=request.POST.get('lname')
        p2.restaurant_name=request.POST.get('restaurant')
        p2.phone=request.POST.get('ph')
        p2.email=request.POST.get('mail')
        p2.location=request.POST.get('location')                 
        p2.type_of_restaurant=request.POST.get('type')
        p2.no_of_staff=request.POST.get('staff')
        p2.authorised_person=request.POST.get('authorised')
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        photo=fs.save(photo.name,photo)
        image1 =fs.url(photo)
        p2.photo = image1
        p2.status=request.POST.get('status')
        p2.save()
    except:
        p2.first_name=request.POST.get('fname')
        p2.last_name=request.POST.get('lname')
        p2.restaurant_name=request.POST.get('restaurant')
        p2.phone=request.POST.get('ph')
        p2.email=request.POST.get('mail')
        p2.location=request.POST.get('location')                 
        p2.type_of_restaurant=request.POST.get('type')
        p2.no_of_staff=request.POST.get('staff')
    
        p2.authorised_person=request.POST.get('authorised')
        p2.status=request.POST.get('status')

        p2.save()
        return redirect('/viewadmin_restaurant/')

def admin_deleteRestaurant(request,id):
    datas1=restaurant_account.objects.get(id=id)
    datas1.delete()
    return redirect('/admin_viewRestaurant/')

def res_view_foodMenu(request):
    d1=request.session['username']
    d2=food_menu.objects.filter(restaurant_name=d1)
    return render(request,'res_view_foodMenu.html',{'y':d2})

def res_update_foodMenu(request,id):
    datas3=food_menu.objects.get(id=id)
    
    return render(request,'res_update_foodMenu.html',{'x':datas3})

def res_update_foodMenu1(request,id):
    p1=food_menu.objects.get(id=id)
    try:
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

    except:
        p1.restaurant_name=request.POST.get('restaurant')
        p1.menu_name=request.POST.get('menu')
        p1.type=request.POST.get('type')
        p1.cruises=request.POST.get('cruises')
        p1.orgin=request.POST.get('orgin')

        p1.save()
    return redirect('/res_view_foodMenu/')

def res_delete_foodMenu(request,id):
    datas4=food_menu.objects.get(id=id)
    datas4.delete()
    return redirect('/res_view_foodMenu/')

def res_offer(request):
    datas5=request.session['username']
    datas6=food_item.objects.filter(restaurant_name=datas5)
    return render(request,'offer.html',{'y':datas5,'x':datas6})

def offer1(request):
    
    p1=offer()

    p1.restaurant_name=request.POST.get('restaurant')
    p1.menu_item_name=request.POST.get('menu_item')
    p1.offer=request.POST.get('offer')
    p1.start_date=request.POST.get('start')
    p1.end_date=request.POST.get('end')
    p1.details=request.POST.get('details')
    p1.status=request.POST.get('status')

    photo=request.FILES['photo']
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    p1.photo=uploaded_file_url
    p1.save()
    return redirect('/restaurentHome/')

def res_view_foodItem(request):
    data7=request.session['username']
    data8=food_item.objects.filter(restaurant_name=data7)
    return render(request,'res_view_foodItem.html',{'x':data8})

def res_update_foodItem(request,id):
    data2=food_item.objects.get(id=id)
    data3=request.session['username']
    data4=food_menu.objects.filter(restaurant_name=data3)
    return render(request,'res_update_foodItem.html',{'x':data2,'y':data4})

def res_update_foodItem1(request,id):
    p1=food_item.objects.get(id=id)
    try:
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

    except:
        p1.restaurant_name=request.POST.get('restaurant')
        p1.menu_name=request.POST.get('menu')
        p1.menu_item_name=request.POST.get('item')
        p1.quantity=request.POST.get('qty')
        p1.price=request.POST.get('rs')
        p1.type=request.POST.get('type')
        p1.cooking_time=request.POST.get('tym')
        p1.status=request.POST.get('status')

        p1.save()
    return redirect('/res_view_foodItem/')

def res_delete_foodItem(request,id):
    data5=food_item.objects.get(id=id)
    data5.delete()
    return redirect('/res_view_foodItem/')

def user_view_offer(request):
    data6=offer.objects.all()
    return render(request,'user_view_offer.html',{'x':data6})

def user_details(request):
    a2=request.session['username']
    a1=user_account.objects.get(username=a2)
    return render(request,'user_details.html',{'x':a1})

def public_restaurant(request):
    data3=restaurant_account.objects.all()
    return render(request,'public_restaurant.html',{'x':data3})

def public_offers(request):
    dat=offer.objects.all()
    return render(request,'public_offers.html',{'x':dat})

def res_view_offers(request):
    off4=request.session['username']
    off5=offer.objects.filter(restaurant_name=off4)
    return render(request,'res_view_offers.html',{'y':off5})

def res_update_offers(request,id):
    off1=offer.objects.get(id=id)
    off2=request.session['username']
    off3=food_item.objects.filter(restaurant_name=off2)
    return render(request,'res_update_offers.html',{'x':off1})



def offer2(request,id):
    p1=offer.objects.get(id=id)
    try:
        p1.restaurant_name=request.POST.get('restaurant')
        p1.menu_item_name=request.POST.get('menu_item')
        p1.offer=request.POST.get('offer')
        p1.start_date=request.POST.get('start')
        p1.end_date=request.POST.get('end')
        p1.details=request.POST.get('details')
        p1.status=request.POST.get('status')

        photo=request.FILES['photo']
        fs= FileSystemStorage()
        filename=fs.save(photo.name,photo) 
        uploaded_file_url=fs.url(filename)
        p1.photo=uploaded_file_url
        p1.save()

    except:
        p1.restaurant_name=request.POST.get('restaurant')
        p1.menu_item_name=request.POST.get('menu_item')
        p1.offer=request.POST.get('offer')
        p1.start_date=request.POST.get('start')
        p1.end_date=request.POST.get('end')
        p1.details=request.POST.get('details')
        p1.status=request.POST.get('status')
        p1.save()

    return redirect('/restaurentHome/')
    
def res_delete_offers(request,id):
    off6=offer.objects.get(id=id)
    off6.delete()
    return redirect('/res_view_offers')


def cart(request,id):
    crt=food_item.objects.get(id=id)

    return render(request,'cart.html',{'x': crt})


def cart1(request):
    c1=tbl_cart()
    a=request.session['username']
    id=request.POST.get('id')
    c=food_item.objects.get(id=id)
    c1.username=a
    c1.restaurant_name=c.restaurant_name
    c1.menu_name=c.menu_name
    c1.menu_item_name=c.menu_item_name
    c1.quantity=request.POST.get('qty')
    c1.price=c.price
    c1.total_price=int(c1.price)*int(c1.quantity)
    # c1.status=request.POST.get('status')
    # photo=request.FILES['photo']
    # fs= FileSystemStorage()
    # filename=fs.save(photo.name,photo) 
    # uploaded_file_url=fs.url(filename)
    # c1.photo=uploaded_file_url
    c1.photo=c.photo
    c1.save()
    return redirect('/view_restaurant/')

def viewcart(request):
    crt3=request.session['username']
    crt2=tbl_cart.objects.filter(username=crt3,status="available")
    return render(request,'view_cart.html',{'x':crt2})

def order(request,id):
    odr=request.session['username']
    odr1=tbl_cart.objects.get(id=id)
    return render(request,'order.html',{'y':odr,'x':odr1})

def order1(request):
    id=request.POST.get('id')
    c=tbl_cart.objects.get(id=id)
    odr3=tbl_order()

    odr3.username=request.POST.get('user')
    odr3.menu_item_name=request.POST.get('item')
    odr3.resturant_name=request.POST.get('restaurant')
    odr3.order_date=request.POST.get('order_date')
    odr3.status="in-order"
    odr3.payment_mode=request.POST.get('Payment')
    odr3.total_price=request.POST.get('price')
    c.status="in-order"
    odr3.save()
    c.save()
    

    return redirect('/viewcart/')

def view_order(request):
    a=request.session['username']
    odr4=tbl_order.objects.filter(resturant_name=a,status='in-order')

    return render(request,'res_view_order.html',{'x':odr4})

def orderdel(request,id):
    ord5=tbl_order.objects.get(id=id)
    
    ord5.status="order-cancelled"
    ord5.save()
    return redirect('/view_order/')

def orderconf(request,id):
    a=tbl_order.objects.get(id=id)
    a.status="order-approved"
    a.save()
    return redirect('/view_order/')

def user_view_order(request):
    a=request.session['username']
    b=tbl_order.objects.filter(username=a,status='order-approved')
    print(a,"test") 
    return render(request,'view_order.html',{'x':b})

def cancel_order(request):
    a=request.session['username']
    b=tbl_order.objects.filter(username=a,status='order-cancelled')
    return render(request,'cancelled_order.html',{'x':b})