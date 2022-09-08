from rest_framework import generics
from .serializer import BookSerializer
from .models import Book
from .permissions import IsOwnerOrReadOnly


class BookList(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
