from django.shortcuts import render
from crdOrder.models import Product
from crdPost.models import Posts, postCategory
# Create your views here.
def Home(request):
    upcommingP=Product.objects.filter(status='upcomming')
    runningP=Product.objects.filter(status='running')
    endedP=Product.objects.filter(status='ended')

    post = Posts.objects.first()
    category = postCategory.objects.all()

    context = {
        'upcommingP' : upcommingP,
        'runningP' : runningP,
        'endedP' : endedP,
        'post' : post,
        'category' : category,

    }
    return render(request, 'home.html', context)