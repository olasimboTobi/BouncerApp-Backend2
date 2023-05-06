from db.models import User
from db.serializers.register_serializer import RegisterSerializer
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from utils import Util


# Create your view(s) here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                first_name = serializer.validated_data['first_name'],
                last_name = serializer.validated_data['last_name'],
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password'],
                otp_code = Util.generate_otp()
                if User.objects.filter(email=email[0]).exists():
                    return Response({"message": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
                # Verification link
                # current_site = get_current_site(request).domain
                # absolute_url = f'http://{current_site}/ap1/v1/otp/verify'
                absolute_url = "https://bouncerb.netlify.app/verify"

                message = f'''
                    Hi {first_name[0]},\n
                    Thanks for registering an account on Bouncer.\n
                    Please confirm your email address via the link {absolute_url}, using the OTP Code below:\n
                    {otp_code}'''

                data = {
                    'email_subject': 'Verify Email Address for Bouncer',
                    'email_body': message,
                    'to_email': email
                }

                Util.send_email(data)

                user = User.objects.create(
                    first_name=first_name[0],
                    last_name=last_name[0],
                    email=email[0],
                    password=password[0],
                    otp_code=otp_code
                )
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Exception as err:
                return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)
              
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
