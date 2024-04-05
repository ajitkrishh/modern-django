from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    class TYPE(models.IntegerChoices):
        Company = 1
        Transporter = 2
        VehicleOwner = 3
        Driver = 4
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_('username'), max_length=50, unique=True, validators=[username_validator])
    phone_regex = RegexValidator(
        regex=r'^[6-9][0-9]{9}$', 
        message="Phone number must be entered in the format: '9999999999'. only 10 digits allowed."
    )
    # validators should be a list
    phone = models.CharField(_('phone number'), validators=[phone_regex], max_length=10, unique=True)
    UserType = models.IntegerField(choices=TYPE)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'UserType']
    credit = models.PositiveIntegerField(default=1)
    Address = models.TextField(max_length=100, blank=True)
    Account_Holder_Name = models.CharField(max_length=50 , blank=True , null=True)
    Account_Type = models.CharField(max_length=10 , blank=True , null=True)
    Bank_Name = models.CharField(max_length=20 , blank=True , null=True)
    Account_Number = models.CharField(max_length=20 , blank=True , null=True, validators=[RegexValidator(
        regex=r'^\d{10,20}$',message='Length of Account Number should be between 10 and 20 digits!!',
    )])
    IFSC = models.CharField(max_length=11 , blank=True , null=True, validators=[RegexValidator(
        regex=r'^\d{11}$',message='Length of IFSC code is 11 digits!!',
    )])
    UPI_QR_CODE = models.ImageField(upload_to='bank-details/qr-code/')
    objects = CustomUserManager()

    def __str__(self) -> str:
        return f'{self.username}'


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    modified_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='%(class)s_modified_by')

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()

    def restore(self):
        self.deleted_at = None
        self.save()

REQUEST_STATUS = (
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('D', 'Declined'),
    )

class Company(CustomUser, BaseModel):
    Company_Name = models.CharField(_('Company Name'), max_length=100, blank=True)
    
    class Meta:
        verbose_name = "Company"
    def __str__(self):
        return f'{str(self.Company_Name)} '


class Transporter(CustomUser, BaseModel):
    pan_card = models.CharField(_('Pan Card'), max_length=10, blank=True)
    aadhar = models.CharField(_('Aadhar number'), max_length=12, blank=True)
    transport_name = models.CharField(_('Transport Name'), max_length=100, blank=True)
    builti_number = models.PositiveIntegerField(default=1)
    vehicle_under_control = models.ManyToManyField(
        'Vehicle', related_name="transporters", blank=True, through='VehicleRequest')

    class Meta:
        verbose_name = "Transporter"
    def __str__(self):
        return f'{str(self.transport_name)}'


class VehicleOwner(CustomUser, BaseModel):
    class Meta:
        verbose_name = "Vehicle Owner"
    def __str__(self):
        return f'{str(self.user.get_short_name())}'


class Vehicle(models.Model):
    owner = models.ForeignKey(VehicleOwner, on_delete=models.SET_NULL,
                              null=True, blank=True, related_name='owned_vehicles')
    driver = models.OneToOneField(
        'Driver', on_delete=models.SET_NULL, null=True, blank=True)
    vehicle_number = models.CharField(
        _('Vehicle Number'), max_length=10, null=True, blank=True)
    is_vehicle_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Vehicle"
    def __str__(self):
        return f'{self.vehicle_number}'


class Driver(CustomUser, BaseModel):
    license = models.CharField(_('license number'), max_length=10, blank=True)
    aadhar = models.CharField(_('Aadhar number'), max_length=12, blank=True)
    class Meta:
        verbose_name = "Driver"

    def __str__(self):
        return f'{str(self.user.get_short_name())}'

class VehicleRequest(BaseModel):
    vehicle_owner = models.ForeignKey('VehicleOwner', on_delete=models.CASCADE)
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)
    transporter = models.ForeignKey("Transporter", on_delete=models.CASCADE)
    request_status = models.CharField(
        choices=REQUEST_STATUS, max_length=20, blank=False, default=REQUEST_STATUS[0][0])
    
# class Friendship(models.Model):
#     from_user = models.ForeignKey(
#         CustomUser, related_name='from_users', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(
#         CustomUser, related_name='to_users', on_delete=models.CASCADE)
#     status = models.CharField(max_length=1, choices=REQUEST_STATUS)

#     def __str__(self):
#         return f"{self.from_user.username} -> {self.to_user.username} ({self.get_status_display()})"
