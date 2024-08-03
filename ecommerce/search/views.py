from django.shortcuts import render
from django.db.models import Q
from shop.models import Products
# Create your views here.

def p_search(request):
    items=None
    query=""
    if request.method=='POST':
        query=request.POST['s']
        if query:
            items=Products.objects.filter(name__icontains=query)
    return render(request,'search.html',{'items':items,'query':query})