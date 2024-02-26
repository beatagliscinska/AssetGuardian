from django.db.models import (
 DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
 Model, TextField, DecimalField, CASCADE
)


class AssetCategory(Model):
    objects = None
    name = CharField(max_length=128)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "AssetCategories"


class Employee(Model):
    objects = None
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    position = CharField(max_length=128)
    department = CharField(max_length=128)
    manager = CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Asset(Model):
    objects = None
    asset_number = IntegerField(unique=True, null=False)
    category = ForeignKey(AssetCategory, on_delete=DO_NOTHING)
    description = TextField()
    vendor = CharField(max_length=128)
    serial_number = CharField(max_length=128, default=True)
    value = DecimalField(max_digits=10, decimal_places=2)
    assigned_to = ForeignKey(Employee, on_delete=DO_NOTHING)
    purchase_date = DateField()

    def __str__(self):
        return str(self.description)