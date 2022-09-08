from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('reviewer', 'book_name', 'book_author', 'review', 'stars')
        model = Book
