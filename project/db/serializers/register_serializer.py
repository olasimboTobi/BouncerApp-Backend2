from db.models.user_model import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# Create your serializer(s) here.
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255,
        min_length=4,
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(), message='email is already taken',)]
    )
    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password],
        write_only=True
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
