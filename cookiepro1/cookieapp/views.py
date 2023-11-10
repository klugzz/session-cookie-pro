from django.shortcuts import render
def namefn(request):
	response = render(request,'apps/name.html')
	return response

def agefn(request):
	name=request.GET['name']
	response=render(request,'apps/age.html')
	response.set_cookie('name',name)
	return response

def cityfn(request):
	age=request.GET['age']
	response=render(request,'apps/city.html')
	response.set_cookie('age',age)
	return response

def resultfn(request):
	city=request.GET['city']
	age=request.COOKIES['age']
	name=request.COOKIES['name']

	response=render(request,'apps/data.html',{'name':name,'age':age,'city':city})
	return response
# Create your views here.
