from django.db import models

from .constants import TRANSACTION_TYPE_CHOICES
from accounts.models import UserBankAccount

class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount,
        related_name='transactions',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        null=True
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        null=True
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES,
        null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Transaction ID: {self.pk}, Account: {self.account.account_no}, Type: {self.get_transaction_type_display()}"

    class Meta:
        ordering = ['timestamp']
