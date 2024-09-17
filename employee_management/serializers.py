from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class LoginSerializer(serializers.ModelSerializer):
	username = serializers.CharField(max_length=255, min_length=3)
	password = serializers.CharField(max_length=68, min_length=6, write_only=True)

	class Meta:
		model = CustomUser
		fields = ['username', 'password']

	def validate(self, attrs):
		username = attrs.get('username', '')
		password = attrs.get('password', '')
		user = authenticate(username=username, password=password)

		if user is None:
			raise AuthenticationFailed('Invalid credentials, try again')

		attrs['user'] = user
		return attrs
