from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from db.models import User
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from db.serializers.login_serializer import LoginSerializer


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            try:
                user = User.objects.get(email=email)
                if not user.is_verified:
                    return Response({"message": "Please verify your email first"}, status=status.HTTP_400_BAD_REQUEST)
                if user.password == password:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({
                    'email': user.email,
                    'token': token.key,
                    }, status=status.HTTP_200_OK)
                return Response({"message": "Incorrect Password"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"message": "Invalid Login"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
