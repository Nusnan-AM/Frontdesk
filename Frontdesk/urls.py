"""
URL configuration for Frontdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from deskapp.passengerViews import PassengerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PassengerView.login, name='user_login'),
    path('passenger/', PassengerView.passenger, name='passenger'), 
    path('passenger-create/', PassengerView.passengerCreate, name='passenger_create'), 
    path('passenger/<int:id>/', PassengerView.passengerDetailsView, name='passenger_view'),
    path('passenger/<int:id>/edit/', PassengerView.passengerEdit, name='passenger_edit'),
    path('passenger/<int:id>/delete/', PassengerView.passengerDelete, name='passenger_delete'),
    path('search/', PassengerView.search, name='passenger_search'),
    path('logout/', PassengerView.logout, name='user_logout'),
]

