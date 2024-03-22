from django.shortcuts import render
from rest_framework import viewsets

from service.models import Book, Borrowing, Payment
from service.serializers import BookSerializer, BorrowingSerializer, PaymentSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = (JWTAuthentication, )
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
