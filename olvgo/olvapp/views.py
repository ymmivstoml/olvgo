from django.shortcuts import render,HttpResponse
from olvapp.models import Customer
from olvapp.forms import CustomerForm
from django.views.generic import CreateView,TemplateView
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class ThankView(TemplateView):
    template_name = 'thankyou.html'

def guaform(request,pk):

    
    theurl = request.get_full_path()
    orderid = theurl[10:]

    if orderid.find("-") == 2 and orderid.count("-") == 3:
        print("Olive Barcode")
    else:
        print("Order id")

    form = CustomerForm(initial={'order_id':orderid})

    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('thank'))
        else:

            HttpResponse("Error from invalid")

    return render(request,'customer_form.html',{'form':form})
