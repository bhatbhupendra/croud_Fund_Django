from crdOrder.models import crdOrder
from django.db import models
from django.utils import timezone

# Create your models here.
class redeemReq(models.Model):
    PAYOPT = (
        ('Bank Transfer','Bank Transfer'),
        ('esewa', 'esewa'),
        ('khalti', 'khalti'),
    )
    STATUS = (
        ('pending','pending'),
        ('redeemed', 'redeemed'),
    )
    order_redeem_code = models.CharField(max_length=500,null=True)
    payOpt=models.CharField(max_length=50,null=True, choices=PAYOPT)
    payToAdress=models.CharField(max_length=50,null=True)
    payToName=models.CharField(max_length=50,null=True)
    order=models.ForeignKey(crdOrder,on_delete=models.CASCADE, null=True, blank=True)
    status=models.CharField(max_length=50,null=True, choices=STATUS)
    Remark = models.TextField(max_length=150,null=True)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.order.name   
    
    class Meta:
        verbose_name="Redeem Request"
        verbose_name_plural="Redeem Requests"