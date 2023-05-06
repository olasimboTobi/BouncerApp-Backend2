from rest_framework import serializers


class LoginSerializer(serializers.Serializer):      
    email = serializers.EmailField(max_length=200, required=True)
    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'},
        write_only=True
    )
