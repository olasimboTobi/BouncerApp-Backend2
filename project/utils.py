import random
from django.core.mail import send_mail
from decouple import config


class Util:
    # Generate OTP
    @staticmethod
    def generate_otp():
        otp_code = random.randrange(100000, 1000000)
        return otp_code

    # Send email
    @staticmethod
    def send_email(data):
        email_subject = data['email_subject']
        message = data['email_body']
        email_from = config('EMAIL_HOST_USER', default='dummy@gmail.com')
        email_to = data['to_email']
        html_format = data['email_body']
        try:
            send_mail(email_subject, message, email_from, email_to,
                      fail_silently=False, html_message=html_format)
        except Exception as err:
            print(str(err))
