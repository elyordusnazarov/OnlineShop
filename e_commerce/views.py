from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *
import json
from django.http import JsonResponse




def signup_view(request):
    form = Profile_Form(request.POST)
    if form.is_valid():
        form.save()

        username = request.POST.get("username")
        password = request.POST.get("password1")
        
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        # print(username, password)
    else:
        print('is not valid ..')


    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def log_out(request):
    user = request.user
    if user:
        logout(request=request)
        return redirect('index')


def log_in(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        if request.user.username == '':
            user = authenticate(request, username=username, password=password)
            if user:
                login(request=request, user=user)
                return redirect('index')
            else:
                return HttpResponse("Username yoki password xato")


    return render(request, 'login.html')

# ///////////////////////////////////////////////

def IndexView(request):
    categories = Category.objects.all()
    products=Products.objects.all()
    topsold=[]
    for i in products:
        savatcha=Savatcha.objects.filter(product=i)
        soni=0
        for j in savatcha:
            soni+= j.quantity
    
        if soni>=1:
            topsold.append({
                'soni':soni,
                'product':i
    })

    if len(topsold) <=15:
        data=[]
        for i in topsold:
            data.append(i['product'])
        context = {
        'categories': categories,
        'topsold':data
    }
 
    else:
        topsold.sort()
        data=topsold[:10]
        context = {
        'category': category,
        'topsold':data
    }

    if request.method == "POST":
        data= json.loads(request.body)
        category_id = data['category']
        products = Products.objects.filter(category_id=category_id)

        data = []
        for i in products:
            data.append({
                'name':i.name,
                'image':i.imageURL,
                'price':i.price,
                'id':i.id
            })

        return JsonResponse({'data': data})
   

    return render(request, 'index.html', context)


# ////////////////////////////////////////////////////



def CartView(request):
    # savatcha=Savatcha.objects.filter(user=request.user,status='progress')
    savatcha=Savatcha.objects.all()
    data=[]
    for i in savatcha:
        total=i.quantity *i.product.price
        data.append({
            'id':i.product.id,
            'name':i.product.name,
            'price':i.product.price,
            'image':i.product.imageURL,
            'description':i.product.description,
            'quantity':i.quantity,
            'total':total
        })

    context={
        'savatcha':data,
    }

    return render(request,'cart.html',context)

def addToCart(request):
    if request.method=='POST':
        data=json.loads(request.body)
        product_id=data['product_id']
        product , bol = Savatcha.objects.get_or_create(user=request.user,product_id=product_id)
        if bol==False:
            product.quantity+=1
            product.save()

        print(data)
        return JsonResponse({'data':'ok'})


def  minusproduct(request):
    if request.method=='POST':
        data=json.loads(request.body)
        product_id=data['product_id']
        print(product_id)
        savatcha=Savatcha.objects.get(user=request.user,product_id=product_id)
        print(savatcha.quantity)
        if savatcha.quantity<=1:
            savatcha.delete()
            print('savatcha o\'chirildi')
        else:
            savatcha.quantity-=1
            savatcha.save()
       
 

        return JsonResponse({'data':'ok'})




def CheckoutView(request):
    return render(request,'checkout.html',{})

def BlogSingleSidebar(request):
    return render(request,'blog-single-sidebar.html')
