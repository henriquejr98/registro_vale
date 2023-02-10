from django.forms import ModelForm
from .models import Register

class LoanForm(ModelForm):
    class Meta:
        model = Register
        fields = ['amount', 'employee']
