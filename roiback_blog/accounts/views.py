from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Estas logueado ahora')
            return redirect('home')
        else:
            messages.error(request, 'Credenciales invalidas')
            return redirect('login')
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Este usuario ya esta registrado')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Este email ya esta registrado')
                    return redirect('signup')
                else:        
                    clean_email = request.POST.get('email')
                    email_base, prov = clean_email.split('@')
                    domain, ext = prov.split('.')
                    if domain == 'roiback':
                        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password, is_staff=True, is_superuser=True)
                        auth.login(request, user)
                        messages.success(request, 'Estas logueado')
                        return redirect('login')
                        user.save()
                        messages.success(request, 'Te has registrado exitosamente')
                        return redirect('login')
                    else:
                        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                        auth.login(request, user)
                        messages.success(request, 'Estas logueado')
                        return redirect('login')
                        user.save()
                        messages.success(request, 'Te has registrado exitosamente')
                        return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')
