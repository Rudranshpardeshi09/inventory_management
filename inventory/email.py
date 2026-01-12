from django.core.mail import send_mail
from django.conf import settings
import os

HEAD_EMAIL = os.getenv("EMAIL_HOST_USER")

def notify_head(subject, html_message):
    send_mail(
        subject=subject,
        message="This email requires HTML support.",  # fallback
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[HEAD_EMAIL],
        html_message=html_message,  # ✅ THIS IS THE KEY
        fail_silently=False,
    )
