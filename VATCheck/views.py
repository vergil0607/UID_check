# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def hello_geek(request):

	# This will return Hello Geeks
	# string as HttpResponse
	return HttpResponse("Hello Geeks")


