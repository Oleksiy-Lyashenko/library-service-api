from django.db import models


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = 'HARD'
        SOFT = 'SOFT'

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(
        max_length=4,
        choices=CoverChoices.choices,
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Borrowing(models.Model):
    borrow_date = models.DateTimeField(auto_now=True)
    expected_return_date = models.DateTimeField()
    actual_return_date = models.DateTimeField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowings")
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Borrowing: {self.book.title}'

    class Meta:
        ordering = ["-borrow_date"]


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING'
        PAID = 'PAID'

    class TypeChoices(models.TextChoices):
        PAYMENT = 'PAYMENT'
        FINE = 'FINE'

    status = models.CharField(
        max_length=7,
        choices=StatusChoices.choices
    )
    type = models.CharField(
        max_length=7,
        choices=TypeChoices.choices
    )
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE, related_name="payments")
    session_url = models.URLField()
    session_id = models.CharField(max_length=255)
    money_to_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Payment: {self.id} ({self.status})'

