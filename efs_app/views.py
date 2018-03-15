from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def IndexPage(request):
    template_name = "index.html"
    return render(request, template_name)