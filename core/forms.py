from django.forms import ModelForm
from .models import Company


class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['postal_code'].widget.attrs['cols'] = 30
        self.fields['postal_code'].widget.attrs['rows'] = 1
        self.fields['description'].widget.attrs['cols'] = 40
        self.fields['description'].widget.attrs['rows'] = 3

    class Meta:
        model = Company
        fields = ['name', 'phone', 'address', 'postal_code', 'district', 'url', 'photo', 'description', 'category']
