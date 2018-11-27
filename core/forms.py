from django.forms import ModelForm
from .models import Company


class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['postal_code'].widget.attrs['cols'] = 25
        self.fields['postal_code'].widget.attrs['rows'] = 1
        self.fields['description'].widget.attrs['cols'] = 20
        self.fields['description'].widget.attrs['rows'] = 1

    class Meta:
        model = Company
        fields = ['name', 'phone', 'address', 'postal_code', 'district', 'url', 'photo', 'description', 'category']
