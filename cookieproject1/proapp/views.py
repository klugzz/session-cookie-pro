from django.shortcuts import render
def cookiefn(request):
	count=int(request.COOKIES.get('countcookie',0))
	newcount=count+1
	response=render(request,'apps/home.html',{'c':newcount})
	response.set_cookie('countcookie',newcount)
	return response
# Create your views here.
