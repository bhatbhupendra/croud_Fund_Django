from django.db import models
from crdPost.models import postCategory
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
pSTATUS = (
        ('upcomming','upcomming'),
        ('running', 'running'),
        ('ended', 'ended'),
    )

oSTATUS = (
        ('Redeemed','Redeemed'),
        ('notRedeem', 'notRedeem'),
        ('notYetTime', 'notYetTime'),
    )

PAYOPT = (
        ('Bank Transfer','Bank Transfer'),
        ('esewa', 'esewa'),
        ('khalti', 'khalti'),
    )

class Product(models.Model):
    name=models.CharField(max_length=50,null=True)
    description = models.TextField(max_length=1500,null=True)
    category = models.ForeignKey(postCategory , on_delete=models.CASCADE , null=True)

    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)
    status=models.CharField(null=True, max_length=20, choices=pSTATUS)

    image=models.ImageField(upload_to='Product/')
    slug=models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)    
    
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"



class crdOrder(models.Model):
    orderId=models.IntegerField(null=True)
    nonce=models.IntegerField(null=True)
    order_type = models.ForeignKey('Product' , on_delete=models.CASCADE , null=True, blank=True)
    name = models.CharField(max_length=50,null=True)
    ph_no=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    payment=models.CharField(max_length=20, null=True,choices=PAYOPT)
    order_redeem_code = models.CharField(max_length=500,null=True)
    amount= models.IntegerField(null=True)
    payment_screen_short=models.ImageField(upload_to='payments/', null=True)
    status = models.CharField(max_length=50,null=True,choices=oSTATUS)
    date=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.order_type.name)
        super(crdOrder,self).save(*args,**kwargs)    
    
    class Meta:
        verbose_name="Order"
        verbose_name_plural="Orders"