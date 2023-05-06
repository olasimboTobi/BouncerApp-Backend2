from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import  AllowAny
from db.serializers import  SetNewPasswordSerializer
from db.models import User
from django.shortcuts import get_object_or_404


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data["otp"]
            user_email = serializer.validated_data["email"]
            new_password = serializer.validated_data["new_password"]
            user = get_object_or_404(User, email=user_email)

            if user.otp_code == otp:
                user.password = new_password
                user.save()
                return Response({"Success": "Password reset succesful"}, status=status.HTTP_200_OK)

            return Response({"Error": "Incorrect otp code"}, status=status.HTTP_400_BAD_REQUEST)

        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            