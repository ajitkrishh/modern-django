from abc import abstractmethod
from .models import InvoiceLine


class InvoiceLineMixin:
    @abstractmethod
    def get_invoice_line(self, *args, **kwargs) -> InvoiceLine:
        pass
