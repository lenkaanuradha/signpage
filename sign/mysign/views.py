from django.shortcuts import render

# Create your views here.
def setcookies(request):
    response=render(request,'setcookies.html')
    response.set_signed_cookie('name','divya',salt='nm')
    return response

def getcookies(request):
    name=request.get_signed_cookie('name',salt='nm')
    return render(request,'getcookies.html',{'name':name})

def delcookies(request):
     response=render(request,'deletecookies.html')
     response.delete_cookie('name')
     return response