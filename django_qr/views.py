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

@login_required
def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            label = form.cleaned_data['label']
            content = form.cleaned_data['content']
            qr=qrcode.make(content)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')

            file_name = label.replace(" ", "_").lower() + "_qr.png"

            qr_record = QRCode(user=request.user, label=label, data=content)
            qr_record.image.save(file_name, ContentFile(buffer.getvalue()), save=False)
            qr_record.save()



            # Generate QR code from the content
            # qr = qrcode.make(content)
            # file_name = label.replace(" ", "_").lower() + "_qr.png"
            # file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            # qr.save(file_path)

            # qr_url = os.path.join(settings.MEDIA_URL, file_name)

            return render(request, 'qr_result.html', {
                'file_name': file_name,
                'label': label,
                'content': content,
                'qr_url': qr_record.image.url,
            })

    else:
        form = QRCodeForm()
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
