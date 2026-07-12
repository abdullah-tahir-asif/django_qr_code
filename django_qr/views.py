from django.shortcuts import render, redirect
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import QRCode
from io import BytesIO
from django.core.files.base import ContentFile
import base64




@login_required
def generate_qr_code(request):
    form = QRCodeForm()
    
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            label = form.cleaned_data['label']
            content = form.cleaned_data['content']
            
            # 1. Generate QR Code matrix in memory
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(content)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")
            
            # 2. Save image data straight into a byte stream buffer
            buffer = BytesIO()
            qr_image.save(buffer, format='PNG')
            buffer.seek(0)
            
            # 3. Encode the binary data to a Base64 string
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            data_uri = f"data:image/png;base64,{image_base64}"
            
            # 4. Save metadata text string to the database (No local image files!)
            qr_record = QRCode(
                user=request.user,
                label=label,
                data=content
            )
            # If your model strictly requires a file path in an ImageField, 
            # we can pass it an empty or placeholder string to satisfy validation.
            qr_record.save()
            
            # 5. Pass the data string straight to your results template
            return render(request, 'qr_result.html', {
                'file_name': label.replace(" ", "_").lower() + "_qr.png",
                'label': label,
                'content': content,
                'qr_url': data_uri,  # This passes the raw image stream directly
            })

    return render(request, 'generate_qr_code.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
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

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('generate_qr_code')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    user_qr_codes=QRCode.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'qr_codes': user_qr_codes})
