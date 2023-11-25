from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import SignupForm, LoginForm,ContactusForm,OrderForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ContactusModel,OrderModel
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.db.models import Q


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass


class Aboutus(View):
    def get(self, request):
        return render(request, 'aboutus.html')

    def post(self, request):
        pass


class Contactus(View):
    def get(self, request):
        form=ContactusForm()
        d={'form':form}
        return render(request, 'contactus.html',d)

    def post(self, request):
        cont=ContactusForm(request.POST)
        if cont.is_valid():
            cont.save()
            messages.success(request,'Your Feedback Saved Successfully !')
        return redirect('contactus')


class Services(View):
    def get(self, request):
        return render(request, 'services.html')

    def post(self, request):
        pass


class Orders(View):
    def get(self, request):
        form=OrderForm()
        d={'form':form}
        return render(request,'orders.html',d)

    def post(self, request):
        om=request.POST['srch']
        b=Q(orderid__icontains=om) | Q(mobileno__icontains=om)
        myuser=OrderModel.objects.filter(b) 
        d={'myuser':myuser}
        return render(request,'orders.html',d)

class Radio(View):
    def get(self,request):
        form=OrderForm()
        d={'form':form}
        return render(request,'orders.html',d)

    def post(self,request):
        a=request.POST['rad']
        e=Q(orderid__icontains=a) | Q(mobileno__icontains=a)
        myuser=OrderModel.objects.filter(e)
        d={'myuser':myuser}
        return render(request,'orders.html',d)

    
'''def Radio(request):
    if request.method=='POST':
        select=request.POST.get('rad')
        d={'select':select}
        return render(request,'orders.html',d)
        myuser=OrderModel.objects.all()
    d={'myuser':myuser}
    return render(request,'ordertable.html',d)'''


def Ordertable(request):
    if request.method=='POST':
        ordmob=request.POST['srch']
        a=Q(orderid__icontains=ordmob) | Q(mobileno__icontains=ordmob)
        myuser=OrdertableModel.objects.filter(a)
        d={'myuser':myuser}
        return render(request,'ordertable.html',d)
    myuser=OrderModel.objects.all()
    d={'myuser':myuser}
    return render(request,'ordertable.html',d)


def Delete(request,eid):
    ob = OrderModel.objects.get(id=eid)
    ob.delete()
    return redirect('orders')



class Signup(View):
    def get(self, request):
        form = SignupForm()
        d = {'form': form}
        return render(request, 'signup.html', d)

    def post(self, request):
        form=SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']
        user = User.objects.create_user(username=username,email=email,password=password)
        user.first_name = name
        user.last_name = contact
        user.save()
        form.save()
        return redirect('signup')


class Login(View):
    def get(self, request):
        form1= LoginForm()
        d = {'form': form1}
        return render(request, 'login.html', d)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Invalid Username Or Password')
            return redirect('login')




class Courier(View):
    def get(self,request):
        return render(request,'courier.html')

    def post(self,request):
        pass

class Payment(View):
    def get(self,request):
        return render(request,'payments.html')

    def post(self,request):
        pass


def logout(request):
    auth_logout(request)
    return redirect('login')


