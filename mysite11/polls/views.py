from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Score

# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST['yourname']
        email=request.POST['mail']
        number=request.POST['mobile']

        mobile=Score()
        mobile.yourname=name
        mobile.mail=email
        mobile.mobile=number
        mobile.save()
    return render(request,"polls/index.html")