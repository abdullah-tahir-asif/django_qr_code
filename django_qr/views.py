from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings



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
   
