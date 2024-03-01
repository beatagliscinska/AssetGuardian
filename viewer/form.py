import re
from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.forms import CharField, ModelForm
from viewer.models import Asset, Employee


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


def capitalized_validator_manager(value):
    first_name, last_name = value.split(' ', 1)
    if not (first_name[0].isupper() and last_name[0].isupper()):
        raise ValidationError('Both first and last names must be capitalized.')


class PastMonthField(forms.DateField):
    widget = forms.DateInput(attrs={'type': 'date'})
# Custom form field for date input with a 'date' type widget.

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class AssetForm(ModelForm):
    vendor = CharField(validators=[capitalized_validator])

    purchase_date = PastMonthField()

    # def clean_description(self):
    #     description = self.cleaned_data.get('description')
    #     if not description.strip():
    #         raise ValidationError("Description field cannot be empty.")
    # #     return description
    #
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_serial_number(self):
        """
        Custom validation method to ensure serial number uniqueness.
        Raises a validation error if a duplicate serial number is found.
        """
        serial_number = self.cleaned_data['serial_number']
        asset_exists = Asset.objects.filter(serial_number=serial_number).exists()
        if asset_exists:
            raise forms.ValidationError("Serial number already exists. Please provide a unique serial number.")
        return serial_number

    class Meta:
        model = Asset
        fields = '__all__'


class EmployeeForm(ModelForm):
    name = CharField(validators=[capitalized_validator], required=True)
    surname = CharField(validators=[capitalized_validator], required=True)
    manager = CharField(validators=[capitalized_validator_manager], required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Employee
        fields = '__all__'
