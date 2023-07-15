from typing import FrozenSet
from django.shortcuts import redirect, render
from .models import Product,crdOrder
from .forms import crdOrderForm
from django.http import HttpResponse, HttpResponseRedirect
from . algo import orderIdGenerator, order_redeem_codeGenerator,nonceGenerator
from django.contrib import messages

# Create your views here.
def productList(request):

    upcommingP=Product.objects.filter(status='upcomming')
    runningP=Product.objects.filter(status='running')
    endedP=Product.objects.filter(status='ended')

    context ={
        'upcommingP' : upcommingP,
        'runningP' : runningP,
        'endedP' : endedP,
    }
    return render(request, 'product_list.html', context)


def productOrder(request,slug):
    product = Product.objects.get(slug=slug)
    if product.status=='upcomming' or product.status=='ended':
        messages.info(request, 'Sorry The Event or Product is ended or upcoming.')
        return redirect('home:main-page')
    
    form = crdOrderForm()

    if request.method == 'POST':
        form = crdOrderForm(request.POST, request.FILES)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.orderId=orderIdGenerator()
            new_form.order_type=product
            new_form.nonce=nonceGenerator()
            new_form.order_redeem_code=order_redeem_codeGenerator(new_form.name, new_form.ph_no, new_form.orderId, new_form.nonce)
            new_form.status='notYetTime'
            new_form.save()
            messages.info(request, 'Order has been placed.')
            messages.info(request, 'Be patient. We\'ll send you order id and redeen code after your order is varified by the admin.')
            return redirect('products:product_list')

    context ={
        'product' : product,
        'form' : form,
    }
    return render(request, 'order_detail.html', context)


def productSummery(request,slug):
    parent = Product.objects.get(slug=slug) #prder_type
    if parent.status=='upcomming' or parent.status=='running':
        messages.info(request, 'Sorry The Event is not ended.')
        return redirect('home:main-page')
    else:
        order_set = parent.crdorder_set.all() # getting all child of the parent
        

    context = {
        'product' : parent,
        'order_set' : order_set,

    }
    return render(request, 'ended_product_summery.html', context)



