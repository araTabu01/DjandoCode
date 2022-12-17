from django.shortcuts import render,HttpResponse
from django.contrib import messages
from datetime import datetime
from home.models import Contact
def index(request):
	# return HttpResponse('this is home page')
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name=name, email=email, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

