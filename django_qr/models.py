from django.db import models
from django.contrib.auth.models import User

class QRCode(models.Model):
    # 1. Kis user ne banaya (Foreign Key)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qr_codes')
    
    # 2. QR code ka naam (Label)
    label = models.CharField(max_length=255, default="My QR Code")
    
    # 3. QR code ke andar ka data/URL
    data = models.TextField()
    
    # 4. QR code ki image file kahan save hogi
    image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    # 5. Kis time par bana
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.label}"