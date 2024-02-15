import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import (
    CharField, DateField, IntegerField, ModelForm
)

from viewer.models import Asset


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class AssetForm(ModelForm):
    description = CharField(validators=[capitalized_validator], required=True,
                            error_messages={'required': 'This field cannot be empty.'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Asset
        fields = '__all__'
        error_messages = {
            'description': {
                'null': "This field cannot be empty."
            }
        }

    vendor = CharField(validators=[capitalized_validator])
    purchase_date = PastMonthField()

    def clean_description(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        description = self.cleaned_data.get('description')
        if description is None or description.strip() == '':
            raise ValidationError("Description field cannot be empty.")
        return self.cleaned_data
