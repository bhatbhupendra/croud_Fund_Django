from django.shortcuts import render,redirect
from django.contrib import messages
from crdOrder.models import crdOrder
from .forms import redeemReqForm
from .models import redeemReq


# Create your views here.

def redeemDetail(request):
    #getting particular order by redeem code
    if request.method == 'POST':
        form = request.POST
        redeem_code = form["code"]

        try:    
            already_redeemed = redeemReq.objects.filter(order_redeem_code=redeem_code)

            if already_redeemed.first().order_redeem_code == redeem_code:
                messages.info(request, 'Redeem Request is already Placed or the code is cashed out...')
                return redirect('home:main-page')
        except:
            pass


        try:
            order = crdOrder.objects.get(order_redeem_code=redeem_code)
            redeemForm = redeemReqForm(initial={'order_redeem_code':redeem_code}) #JUST SENDING FORM IN THIS PAGE

            #delattr(order, order_redeem_code)
            context ={
                'order' : order,
                'redeemForm' :redeemForm,
            }
            return render(request, 'order-redeem.html', context)

        except:
            messages.info(request, 'Wrong Redeem Code..Make sure You have currect one.')
            return redirect('home:main-page')

    
    else:
        messages.info(request, 'Bad Request.. Please contact Costumer Care.')
        return redirect('home:main-page')


def redeemRequest(request):
    form = redeemReqForm()
    if request.method == 'POST':
        form = redeemReqForm(request.POST)
        print(form)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.order=getOrder(new_form.order_redeem_code)
            new_form.status='pending'
            
            if crdOrder.objects.get(order_redeem_code=form.cleaned_data.get('order_redeem_code')):
                new_form.save()
                messages.info(request, 'Redeem Request is placed..Your transection is completed shortly.')
                return redirect('home:main-page')
            else:
                messages.info(request, 'Wrong Redeem Code..Make sure You have currect one.')
                return redirect('home:main-page')

        else:
            messages.info(request, 'Sorry..Form is not valid')
            return redirect('home:main-page')



def getOrder(code):
    code=code
    return crdOrder.objects.get(order_redeem_code=code)