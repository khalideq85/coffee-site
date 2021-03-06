from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('coffee', views.coffee, name='coffee'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('allproducts', views.allproducts, name='allproducts'),

]
