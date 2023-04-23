from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 1. login (& display login failure)
    # if login success, redirect to home
    path('login/', auth_views.LoginView.as_view(template_name='rider/login.html', redirect_authenticated_user=True),
         name='login'),
    # 2. create an account
    path('create_account/', views.create_account, name='create_account'),
    # 3+4. driver page + driver registration
    path('driver/', views.driver, name='rider-driver'),
    # 5. main user page after login ("Ride")
    path('', views.home, name='rider-home'),
    path('home/', views.home, name='rider-home'),
    
    # 6. ride details
    path('ride_details', views.ride_details, name='rider-ride_details'),

    # 7. sharer page ("join a ride")
    path('sharer/', views.sharer, name='rider-sharer'),

    # 8. logout
    #  if logout success, redirect to login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
'''[
    # 7. sharer page ("join a ride")
    path('sharer', views.sharer, name='rider-sharer'),
]'''
