from utils import Util
from db.models.user_model import User
from db.serializers.forgot_password_serializer import ForgotPasswordSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                email = serializer.validated_data["email"]
                user = get_object_or_404(User, email=email)
                otp_code = Util.generate_otp()
                user.otp_code = otp_code
                user.save()
                current_site = get_current_site(request=request).domain 
                print(current_site)
                # absurl = f"http://{current_site}/api/v1/reset-password/"
                absurl = "https://bouncerb.netlify.app/forgot-password"
                email_body = f"Hello, \n Use this link {absurl} with OTP {otp_code} to reset your password \n"  
                data = {'email_body': email_body, 'to_email': [email], 'email_subject': 'Reset your password on Bouncer'}
                Util.send_email(data)
                return Response({"message": "OTP sent to your mail"}, status=status.HTTP_200_OK)
              
            except Exception as error:
                return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
