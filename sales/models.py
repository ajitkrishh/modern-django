from django.db import models
from UserAccount.models import CustomUser, BaseModel


class Invoice(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class product(BaseModel):
    name = models.CharField(max_length = 100)
    price = models.FloatField(default=0)
    invoice_number = models.ForeignKey(Invoice, on_delete=models.RESTRICT , null=True , blank=True)
