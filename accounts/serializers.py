from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'bio',
            'profile_picture',
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        Token.objects.create(user=user)
        return user
