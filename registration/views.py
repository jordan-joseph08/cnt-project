from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def register(request):
    if request.method== 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.create_user(username=email, password=password,first_name=first_name, last_name=last_name)
        user.save()
        print('user created')
        return redirect('home/')
    return render(request, 'registration.html')
