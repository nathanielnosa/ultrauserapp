from django.core.mail import send_mail
from django.conf import settings


def sendMail(email):
    subject = "Welcome to ultra application"
    message = f'''
                    This is an onboarding message, to show that
                    you are now a registered user !
            '''
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,)
        