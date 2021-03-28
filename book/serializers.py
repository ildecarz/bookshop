from rest_framework import serializers
from .models import *

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
        


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
            
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'
            