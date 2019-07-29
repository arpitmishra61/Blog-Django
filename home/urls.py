from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signUp, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('public-blogs', views.publicBlogs, name='publicBlogs'),
    path('my-blogs', views.myBlogs, name='myBlogs'),
    path('show', views.show, name='show')

]
