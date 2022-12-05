from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length = 45)
    password  = serializers.CharField(min_length = 8,write_only=True)


    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been registered")

        return super().validate(attrs)

# to hash the password on creation of the user
    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

# Will create toekn for the specific user
        Token.objects.create(user=user)

        return user

