from datetime import timezone
from enum import Enum

from django.db import models


class CoverChoices(Enum):
    HARD = 'HARD'
    SOFT = 'SOFT'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(
        max_length=4,
        choices=[(choice.value, choice.name) for choice in CoverChoices]
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Borrowing(models.Model):
    borrow_date = models.DateField(default=timezone.now)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(blank=True, null=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Borrowing: {self.book.title} by {self.user.username}'

