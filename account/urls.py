from django.urls import path
from . import views


urlpatterns = [
    path('',views.startpage,name='startpage'),
    path('home/',views.home,name='home'),
    path('userhomepage/',views.userhomepage,name='userhomepage'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutuser,name='logout'),
    path('addproductuser/',views.addproductuser1,name='addproductuser'),
    path('purchased/',views.purchased,name='purchased'),
    path('skip/',views.skip,name='skip')
]