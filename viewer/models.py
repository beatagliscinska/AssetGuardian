from django.db.models import (
 DO_NOTHING, CharField, DateField, ForeignKey,
 Model, DecimalField
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
    category = ForeignKey(AssetCategory, on_delete=DO_NOTHING)
    description = CharField(max_length=128)
    vendor = CharField(max_length=128)
    serial_number = CharField(max_length=128)
    value = DecimalField(max_digits=10, decimal_places=2)
    assigned_to = ForeignKey(Employee, on_delete=DO_NOTHING)
    purchase_date = DateField()

    def __str__(self):
        return str(self.description)