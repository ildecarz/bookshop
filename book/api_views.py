from rest_framework.views import APIView
from rest_framework import generics
from .serializers import LibrarySerializer, BookSerializer, AuthorSerializer, LeadsSerializer
from .models import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

class LibraryCreateAPIView(generics.CreateAPIView):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

class LibraryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = LibrarySerializer
    queryset = Book.objects.all()

class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorCreateAPIView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Book.objects.all()

class AuthorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AuthorSerializer
    queryset = Book.objects.all()

class LeadsCreateAPIView(generics.CreateAPIView):
    serializer_class = LeadsSerializer
    queryset = Leads.objects.all()
