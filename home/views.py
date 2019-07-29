from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Profile
from .models import Article
from django.http import HttpResponse as res
import json

from django.contrib.auth.models import User


# Create your views here.
def show(request):
        info={
            'name':'arpit',
            'age':30
        }
        return res(json.dumps(info))


def home(request):
    if(request.method == 'GET'):
        if(request.user.is_authenticated):

            return render(request, 'home.html')
        else:
            return redirect('login')
    if(request.method == 'POST'):
        title = request.POST["title"]
        description = request.POST["description"]
        article = Article(title=title, description=description,
                          editor=request.user.email)
        article.save()
        print(request.user.email)

        messages.success(request, "Post uploaded successfully")
        return redirect("home")


def signUp(request):
    if(request.user.is_authenticated):
        return redirect('home')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        username = request.POST['username']
        if(name == '' or email == '' or mobile == ''or password == ''):
            messages.warning(request, "Credentials can't be empty")
            return redirect('signup')
        print(User.objects.filter(email=email))
        if(cpassword != password):
            messages.error(request, "Password did'nt match")
            return redirect('signup')
        else:

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Already Registered')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password,
                    email=email,
                    is_staff=False
                )
                profile = Profile(user=user, name=name, mobile=mobile)

                user.save()
                profile.save()

                messages.success(request, "Registered Successfuly")
                return redirect('login')

    return render(request, 'signUp.html')


def login(request):
    if(request.user.is_authenticated):
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        if(User.objects.filter(username=username).exists()):
            for user in User.objects.filter(username=username):

                if (auth.authenticate(username=username, password=password) == None):
                    messages.error(request, "Password is incorrect")
                    return redirect('login')
                else:
                    user = auth.authenticate(
                        username=username, password=password)
                    auth.login(request, user)
                    return redirect('home')

        else:
            messages.error(request, "Username dosen't exists")

    return render(request, 'login.html')


def logout(request):

    auth.logout(request)

    return redirect('login')


def publicBlogs(request):
    articles = Article.objects.all(
        ).order_by('-date')
    print(articles)
    return render(request, "publicBlogs.html", {'articles': articles})


def myBlogs(request):
    

    articles = Article.objects.filter(
        editor=request.user.email).order_by('-date')
    print(articles)
    return render(request, "myBlogs.html", {'articles': articles})
