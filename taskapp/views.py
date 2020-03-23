from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,request
from django.contrib import messages
from .models import data,iplist
from datetime import date
import json
import requests



# Create your views here.
def homepage(request):
    return render(request,"index.html")


def submitfinal(request):
    name = request.POST['name']
    email = request.POST['email']
    pwd = request.POST['password']
    currentip = request.META.get('REMOTE_ADDR')
    currentdate = date.today()
    if data.objects.filter(email=email).exists():
        messages.success(request, 'User Already Registered')
        return HttpResponseRedirect('/')
    else:
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6LfTFuMUAAAAAPEIJlLwt9PBW-PUzoNHkTy-ZC3U'
        cdata = {
            'secret': secretkey,
            'response': clientkey

        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=cdata)
        response = json.loads(r.text)
        verify = response['success']
        print(verify)
        if verify:
            p = data(name=name, email=email, password=pwd, ipaddress=currentip)
            p.save()
            newcount = 1;
            m = iplist(ip=currentip, count=newcount, idate=currentdate)
            m.save()
            return HttpResponse('success')
        else:
            return HttpResponse('Captcha Verification Faild')









def submitform(request):
    name = request.POST['name']
    email = request.POST['email']
    pwd = request.POST['password']
    currentip = request.META.get('REMOTE_ADDR')
    currentdate = date.today()

    if data.objects.filter(email=email).exists():
        messages.success(request, 'User Already Registered')
        return HttpResponseRedirect('/')
    else:
        if iplist.objects.filter(ip=currentip).exists():
            count = iplist.objects.only('count').get(ip=currentip, idate=currentdate).count
            if count > 3:
                return render(request, "test.html")
            else:
                newcount = count + 1
                iplist.objects.filter(ip=currentip, idate=currentdate).update(count=newcount)
                p = data(name=name, email=email, password=pwd, ipaddress=currentip)
                p.save()
                return HttpResponse('successful')
        else:
            p = data(name=name, email=email, password=pwd, ipaddress=currentip)
            p.save()
            newcount = 1;
            m = iplist(ip=currentip, count=newcount, idate=currentdate)
            m.save()
            return HttpResponse('successful')









