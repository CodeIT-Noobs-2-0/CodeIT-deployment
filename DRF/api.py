from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework.response import Response
from account.models import User, Donor, NGO_Admin
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from rest_framework import generics, permissions
from .serializers import *
from .serializers import UserDisplaySerializer, UserSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserDisplayView(APIView):
    queryset = User.objects.all()
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User.objects.all(), pk=pk)
            serializer = UserSerializer(user)
            return Response({"user": serializer.data})
        users = User.objects.all()
        serializer = UserDisplaySerializer(users, many=True)
        return Response({"users": serializer.data})

class DonorDisplayView(APIView):
    queryset = Donor.objects.all()
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(Donor.objects.all(), pk=pk)
            serializer = DonorSerializer(user)
            return Response({"user": serializer.data})
        users = Donor.objects.all()
        serializer = DonorDisplaySerializer(users, many=True)
        return Response({"users": serializer.data})


class NGOAdminDisplayView(APIView):
    queryset = NGO_Admin.objects.all()
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(NGO_Admin.objects.all(), pk=pk)
            serializer = NGOAdminSerializer(user)
            return Response({"user": serializer.data})
        users = NGO_Admin.objects.all()
        serializer = NGOAdminDisplaySerializer(users, many=True)
        return Response({"users": serializer.data})


class DonatedDisplayView(APIView):
    queryset = Donated.objects.all()
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(Donated.objects.all(), pk=pk)
            serializer = DonatedSerializer(user)
            return Response({"user": serializer.data})
        users = NGO_Admin.objects.all()
        serializer = DonatedDisplaySerializer(users, many=True)
        return Response({"users": serializer.data})


"""     REGISTERTION STARTS FROM HERE           """

class RegisterUser(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer1

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user is not None:
            # A backend authenticated the credentials
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)

        # print(token.key)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key,
            # "token": AuthToken.objects.create(user)[1]
        })

class RegisterDonor(generics.GenericAPIView):
    serializer_class = DonorRegisterSerializer1

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user is not None:
            # A backend authenticated the credentials
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)

        # print(token.key)

        return Response({
            "user": DonorSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key,
            # "token": AuthToken.objects.create(user)[1]
        })

class RegisterNGOAdmin(generics.GenericAPIView):
    serializer_class = NGOAdminRegisterSerializer1

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user is not None:
            # A backend authenticated the credentials
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)

        # print(token.key)

        return Response({
            "user": NGOAdminSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key,
            # "token": AuthToken.objects.create(user)[1]
        })


