from rest_framework import serializers


class VerifyOTPSerializer(serializers.Serializer):      
    otp_code = serializers.CharField(max_length=6)
    email = serializers.EmailField(max_length=200)
