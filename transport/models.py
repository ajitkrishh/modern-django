from django.db import models
from UserAccount.models import Company, Transporter, Vehicle, VehicleOwner, Driver
from django.utils.timezone import now

from sales.utils import InvoiceLineMixin
from sales.models import InvoiceLine

# Create your models here.
class ChallanTemplate(models.Model, InvoiceLineMixin):
    source = models.ForeignKey(
        Company, on_delete=models.RESTRICT, related_name="Loaded_from"
    )
    destination = models.ForeignKey(
        Company, on_delete=models.RESTRICT, related_name="unloaded_at"
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.RESTRICT)
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT)
    transporter = models.ForeignKey(
        Transporter, on_delete=models.RESTRICT, related_name="transporter"
    )
    challan_number = models.DecimalField(max_digits=10, blank=False, decimal_places=0)
    material = models.CharField(max_length=30, null=True)
    Weight_at_loading = models.DecimalField(
        max_digits=10, blank=False, default=0, decimal_places=2
    )
    Weight_at_unloading = models.DecimalField(
        max_digits=10, blank=True, default=0, decimal_places=2
    )
    loading_dt = models.DateField(default=now, blank=True)
    unloading_dt = models.DateField(null=True, blank=True)

    def get_invoice_line(self, invoice_id):
        invoice_line_obj = InvoiceLine(
            name="Challan" + str(self.challan_number),
            template_model="transport.ChallanTemplate",
            template_model_ref_id=self.pk,
            invoice=invoice_id,
        )
        return invoice_line_obj
