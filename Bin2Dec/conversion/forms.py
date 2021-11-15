from django.forms import ModelForm, ValidationError

from .models import Conversion

class ConversionForm(ModelForm):

    def clean_num(self):
        data = self.cleaned_data['num']

        if not data.isdigit():
            raise ValidationError('Invalid num')

        for i in data:
            if i not in '10':
                raise ValidationError('Invalide num')

        return data

    class Meta:
        model = Conversion
        fields = ['num', ]


