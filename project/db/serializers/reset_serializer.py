from rest_framework import serializers


class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6,  write_only=True)
    new_password = serializers.CharField(min_length=6, max_length=68, write_only=True, required=True,
        style={'input_type': 'password'})
    confirm_password = serializers.CharField(min_length=6, max_length=68, write_only=True, required=True,
        style={'input_type': 'password'})

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError("New password and the confirm password does not match")
        return data
