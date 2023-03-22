from django.shortcuts import render,HttpResponseRedirect,redirect
from Market.models import Display
from Market.forms import DisplayForm,NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def create_new_user(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email')
        user = User.objects.create_user(username, password=password, email=email)
        user.save()
        return redirect('HomePage')
    return render(request,'register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print('======================>')
        print(user)
        if user is not None:
            login(request, user)
            return redirect('HomePage')
    return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    return redirect("index")
    
def home_page(request):
    return render(request,'homePage.html',{})

def products_available(request):
    form = DisplayForm()
    if request.method == 'POST':
        form = DisplayForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'names.html', {'form': form})

def list_of_products(request):
    Product_Display=Display.objects.all()
    return render(request,"products.html",{'Product_Display':Product_Display})


def add_to_cart(request, **kwargs):
    if pk := kwargs.get('pk'):
        product = Display.objects.get(pk = pk)
        cart = request.session.get('cart',[])
        items = {'name_of_product':product.name, 'price':product.price}
        cart.append(items)
        request.session['cart'] = cart
        name = request.session['cart']
        return render(request,'Cart_products.html', {'name':name})
    
def remove_from_cart(request,**kwargs):
    if pk:= kwargs.get('pk'):
        import pdb;pdb.set_trace()
        product = Display.objects.get(pk = pk)
        for i in request.session['cart']:
            if i['product_id'] == product.pk:
                request.session['cart'].remove(i)
    return render(request, 'Cart_products.html',{'product':product})
    
# def add_to_cart(request,**kwargs):
#     if pk:=kwargs.get('pk'):
#         item=Display.objects.get(pk=pk)
#         item=AddToCart.objects.create(cart_Id=pk)
#         item.save()
#     item=AddToCart.objects.all()
#     return render(request,'Cart_products',{'item':item})   

