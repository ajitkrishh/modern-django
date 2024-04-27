from django.db import models
from UserAccount.models import CustomUser, BaseModel


class Invoice(BaseModel):
    issuer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="issuer"
    )
    issuee = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="issuee"
    )
    invoice_number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        invoice_lines = self.invoice_lines
        print(invoice_lines)


class InvoiceLine(BaseModel):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="invoice_lines",
    )
    template_model = models.CharField(max_length=30)
    template_model_ref_id = models.PositiveIntegerField()
