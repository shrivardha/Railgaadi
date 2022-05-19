"""Railgaadi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf.urls import url
from users import views as users_views
from train import views as train_views
from django.conf import settings
from django.conf.urls.static import static
re_path=url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',users_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', users_views.profile, name='profile'),
    path('schedule/',train_views.schedule, name='schedule'),
    path('railgaadi/',train_views.railgaadi, name='railgaadi'),
    path('search/',train_views.search,name='search'),
    path('book_detail/(?P<coun>[0-9]+)/(?P<pid>[0-9]+)/(<str:route1>)',train_views.Book_detail,name="book_detail"),
    path('delete_passenger/(?P<pid>[0-9]+)/(?P<bid>[0-9]+)/(<str:route1>)', train_views.Delete_passenger, name="delete_passenger"),
    

    path('card_detail/(?P<total>[0-9]+)/(?P<coun>[0-9]+)/(<str:route1>)/(?P<pid>[0-9]+)', train_views.Card_Detail, name="card_detail"),
    path('my_booking/', train_views.my_booking, name="my_booking"),
    #path('delete_my_booking/(?P<pid>[0-9]+)', train_views.delete_my_booking, name="delete_my_booking"),
    path('delete_my_booking/(?P<pid>[0-9]+)', train_views.delete_my_booking, name="delete_my_booking"),
    path('view_ticket/(?P<pid>[0-9]+)', train_views.view_ticket, name="view_ticket"),
    

    path('p/',users_views.profile, name='p'),


    #path('bookings/',train_views.bookings,name='bookings'),
    path('contact/', users_views.contactus, name='contact'),
    path('cancel/', train_views.cancel, name='cancel'),
    #path('register/',include('users.urls')),
    path('',include('train.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)