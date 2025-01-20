from django.shortcuts import render
from .serializer import PassengerSerializer
from .models import  Passenger
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models


# Create your views here.

class PassengerView(APIView):
    
    def login(request):
        
        if request.user.is_authenticated:
            return redirect('passenger')
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('passenger')
            else:
                return render(request, 'pages/login.html',{"login_error":"Invalid credentials"})
        return render(request, 'pages/login.html')
    
    @login_required
    def logout(request):
        logout(request)
        return redirect('user_login')
    

    
    @login_required
    def passenger(request):
        atributes = {}     
        passengers = Passenger.objects.all()
        atributes['passengers'] = passengers
        return render(request, 'pages/dashboard.html', atributes)
    

    @login_required
    def passengerCreate(request):
        atributes = {}
        if request.method == 'POST':
            data = {
                'registration_number': request.POST.get('registration_number'),
                'passport_number': request.POST.get('passport_number'),
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'nic': request.POST.get('nic'),
                'mobile': request.POST.get('mobile'),
                'telephone': request.POST.get('telephone'),
                'email': request.POST.get('email'),
                'address': request.POST.get('address'),
            }
            
            serializer = PassengerSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                atributes['register_success'] = True
                atributes['open_modal'] = False 
                atributes['form_data'] = None
            else:
                atributes['register_success'] = False
                atributes['form_error_message'] = serializer.errors
                atributes['form_data'] = data
                atributes['open_modal'] = True 

        if request.method == 'GET':
            atributes['form_data'] = None
            atributes['open_modal'] = True

        passengers = Passenger.objects.all()
        atributes['passengers'] = passengers
        return render(request, 'pages/dashboard.html', atributes)
    


    @login_required
    def passengerEdit(request,id):
        atributes = {}
        try:
            if request.method == 'POST':
                if request.POST.get('_method') == 'PATCH' and id:
                    data = {
                        'registration_number': request.POST.get('registration_number'),
                        'passport_number': request.POST.get('passport_number'),
                        'first_name': request.POST.get('first_name'),
                        'last_name': request.POST.get('last_name'),
                        'nic': request.POST.get('nic'),
                        'mobile': request.POST.get('mobile'),
                        'telephone': request.POST.get('telephone'),
                        'email': request.POST.get('email'),
                        'address': request.POST.get('address'),
                    }
                    
                    passenger = Passenger.objects.get(id=id)
                    serializer = PassengerSerializer(passenger, data=request.POST, partial=True)

                    if serializer.is_valid():
                        serializer.save()
                        passengers = Passenger.objects.all()
                        atributes['register_success'] = True
                        atributes['passengers'] = passengers
                    else:
                        atributes['register_success'] = False
                        atributes['form_error_message'] = serializer.errors
                        atributes['form_data'] = data
                        atributes['open_modal'] = True

            if request.method == 'GET':
                    passenger = Passenger.objects.get(id=id)
                    passengers = Passenger.objects.all()
                    atributes['form_data'] = passenger
                    atributes['passengers'] = passengers
                    atributes['open_modal'] = True
                    atributes['open_view_modal'] = False

                    
            return render(request, 'pages/dashboard.html', atributes)
        except Passenger.DoesNotExist:
             return render(request, 'pages/not-found.html', atributes)

         


    @login_required
    def passengerDetailsView(request,id):
        atributes = {}
        try:
            passenger = Passenger.objects.get(id=id)
            passengers = Passenger.objects.all()
            atributes['passengers'] = passengers
            atributes['form_data'] = passenger
            atributes['open_modal'] = False
            atributes['open_view_modal'] = True
            return render(request, 'pages/dashboard.html', atributes)
        except Passenger.DoesNotExist:
            return render(request, 'pages/not-found.html', atributes)


    @login_required
    def passengerDelete(request,id):
        atributes = {}
        try:
            passenger = Passenger.objects.get(id=id)
            if request.method == 'GET':
                atributes['deletePassenger'] = passenger
                atributes['open_delete_model'] = True
            elif request.method == 'POST':
                  if request.POST.get('_method') == 'DELETE' and id:   
                        passenger.delete()
            passengers = Passenger.objects.all()
            atributes['passengers'] = passengers
            return render(request, 'pages/dashboard.html', atributes)
        except Passenger.DoesNotExist:
             return render(request, 'pages/not-found.html', atributes)

    @login_required
    def search(request):
        query = request.GET.get('query')
        passengers = Passenger.objects.filter(models.Q(passport_number__icontains=query) | models.Q(nic__icontains=query))
        return render(request, 'pages/dashboard.html', {'passengers': passengers})

            

        

  

    
  