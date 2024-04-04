# Generated by Django 5.0 on 2024-04-03 18:28

import UserAccount.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '9999999999'. only 10 digits allowed.",
                                regex="^[6-9][0-9]{9}$",
                            )
                        ],
                        verbose_name="phone number",
                    ),
                ),
                (
                    "UserType",
                    models.IntegerField(
                        choices=[
                            (1, "Company"),
                            (2, "Transporter"),
                            (3, "Vehicleowner"),
                            (4, "Driver"),
                        ]
                    ),
                ),
                ("credit", models.PositiveIntegerField(default=1)),
                ("Address", models.TextField(blank=True, max_length=100)),
                (
                    "Account_Holder_Name",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "Account_Type",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ("Bank_Name", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "Account_Number",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Length of Account Number should be between 10 and 20 digits!!",
                                regex="^\\d{10,20}$",
                            )
                        ],
                    ),
                ),
                (
                    "IFSC",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Length of IFSC code is 11 digits!!",
                                regex="^\\d{11}$",
                            )
                        ],
                    ),
                ),
                ("UPI_QR_CODE", models.ImageField(upload_to="bank-details/qr-code/")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", UserAccount.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "license",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="license number"
                    ),
                ),
                (
                    "Aadhar",
                    models.CharField(
                        blank=True, max_length=12, verbose_name="Aadhar number"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("UserAccount.customuser", models.Model),
            managers=[
                ("objects", UserAccount.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Transporter",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "Pan_Card",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Pan Card"
                    ),
                ),
                (
                    "Aadhar",
                    models.CharField(
                        blank=True, max_length=12, verbose_name="Aadhar number"
                    ),
                ),
                (
                    "Transport_Name",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Transport Name"
                    ),
                ),
                ("BuiltiNumber", models.PositiveIntegerField(default=1)),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("UserAccount.customuser", models.Model),
            managers=[
                ("objects", UserAccount.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="VehicleOwner",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("UserAccount.customuser", models.Model),
            managers=[
                ("objects", UserAccount.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "Company_Name",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Company Name"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("UserAccount.customuser", models.Model),
            managers=[
                ("objects", UserAccount.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Vehicle_Number",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Vehicle Number",
                    ),
                ),
                ("is_vehicle_active", models.BooleanField(default=False)),
                (
                    "driver",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="UserAccount.driver",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="owned_vehicles",
                        to="UserAccount.vehicleowner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VehicleRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "Requeststatus",
                    models.CharField(
                        choices=[
                            ("P", "Pending"),
                            ("A", "Accepted"),
                            ("D", "Declined"),
                        ],
                        default="P",
                        max_length=20,
                    ),
                ),
                (
                    "Vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserAccount.vehicle",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "Transporter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserAccount.transporter",
                    ),
                ),
                (
                    "Vehicle_Owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserAccount.vehicleowner",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="transporter",
            name="Vehicle_Under_Control",
            field=models.ManyToManyField(
                blank=True,
                related_name="transporters",
                through="UserAccount.VehicleRequest",
                to="UserAccount.vehicle",
            ),
        ),
        migrations.AddField(
            model_name="transporter",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="transporter",
            name="modified_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(class)s_modified_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]