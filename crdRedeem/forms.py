from datetime import date
from django.forms import ModelForm
from .models import redeemReq

class redeemReqForm(ModelForm):
    class Meta:
        model = redeemReq
        exclude = ['order','date','status']