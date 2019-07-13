from django.shortcuts import render
# import templateview
from django.views.generic import TemplateView
# Create your views here.
# http://ccbv.co.uk/projects/Django/2.2/django.views.generic.base/TemplateView/

# create a simple view class with TemplateView
class HelloDjango(TemplateView):
    # render the home.html file
    template_name = 'home.html'
