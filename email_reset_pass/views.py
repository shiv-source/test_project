from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import SignupForm

# Create your views here.

def home(request):
    data = SignupForm.objects.all()
    return render(request, 'home.html',{'data':data} )

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        logged_in_user = auth.authenticate(username=username,password=password)
        if logged_in_user is not None:
            auth.login(request,logged_in_user)
            return redirect('/')
        else:
            return redirect('/login/')
    else:
        return render(request,'login.html',)

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        if password_1 == password_2:
            signed_user = SignupForm(first_name=first_name,last_name=last_name,
                                     username=username,email=email,phone_no=phone_no,
                                     password_1=password_1,password_2=password_2)
            signed_user.save()
            return redirect('/')
        else:
            return redirect('/signup/')


    else:
        return render(request, 'signup.html', )


def logout(request):
    auth.logout(request)
    return redirect('/')

