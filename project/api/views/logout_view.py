from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


class LogoutAPIView(APIView): 
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"success": "Successfully logged out"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Unable to log out"}, status=status.HTTP_400_BAD_REQUEST)
        