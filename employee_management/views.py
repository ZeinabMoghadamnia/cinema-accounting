from audioop import reverse

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from .serializers import LoginSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer


class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    permission_classes = [AllowAny]

    def get(self, request):
        return Response()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({'message': 'Successfully logged in'},
                            template_name='reports.html')

        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('employee_management:login_page')