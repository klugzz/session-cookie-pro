from django.shortcuts import render
from django.http import HttpResponse
def setcookie(request):
	response = HttpResponse("Cookie Set")
	response.set_cookie('Djangocookie','welcome to systech')
	return response

def getcookie(request):
	t = request.COOKIES['Djangocookie']
	return HttpResponse("SYSTECH GROUP TESTING: "+ t)
# Create your views here.
