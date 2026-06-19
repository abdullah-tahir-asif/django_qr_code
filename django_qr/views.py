from django.shortcuts import render, redirect
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required
def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            restraunt_name = form.cleaned_data['restraunt_name']
            url = form.cleaned_data['url']

            # generate qrcode
            qr= qrcode.make(url)
            file_name = restraunt_name.replace(" ", "_").lower() + "menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            qr_url = os.path.join(settings.MEDIA_URL, file_name)

            return render(request, 'qr_result.html', {'file_name': file_name, 'restraunt_name': restraunt_name, 'qr_url': qr_url})
        

    else:
        form = QRCodeForm()
        return render(request, 'generate_qr_code.html', {'form': form})


            # Here you would generate the QR code using the restraunt_name and url
            # For now, we will just render the form again  
            #  



def signup_view(request):
    if request.method== 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=fullname)
        user.save()
        return redirect('generate_qr_code')
        

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Authenticate the user using the email and password
        
        user = authenticate(username=email, password=password)
        if user:
            login(request,user)
            return redirect('generate_qr_code')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
        

        # Here you would authenticate the user using the email and password
        # For now, we will just render the form again
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


