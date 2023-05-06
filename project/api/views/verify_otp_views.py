from db.models import User
from db.serializers.verify_otp_serializers import VerifyOTPSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny


class VerifyOTPView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)

        if serializer.is_valid():
            code = serializer.validated_data["otp_code"]
            user_email = serializer.validated_data["email"]

            try:
                user = User.objects.get(email=user_email)

                if user.otp_code == code:
                    user.is_verified = True
                    user.save()
                    return Response({"message": "Email Succesfully Activated"}, status=status.HTTP_200_OK)
                return Response({"message": "incorrect otp code"}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist: 
                return Response({"error": "Account not verified. Please provide a valid code"},
                                status=status.HTTP_400_BAD_REQUEST)  
        return Response({"message": "Please enter the email and otp code sent to you"}, status=status.HTTP_400_BAD_REQUEST)
