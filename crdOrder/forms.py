from django.forms import ModelForm
from .models import crdOrder

class crdOrderForm(ModelForm):
    class Meta:
        model = crdOrder
        exclude = ['orderId','order_type','order_redeem_code','status','date','slug', 'nonce']