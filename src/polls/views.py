#from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ebaySearchForm
# Create your views here.
from polls.templatetags.ebayFindingApi import *
from polls.twitterPositivity import *

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
#from core.TwitterPositivity import *

#from .serializers import PostSerializer2, MyOutputSerializer
#from .models import ebaySearch, ebayResults

import requests

class ebaySearchView(TemplateView):
    def get(self, request):
        form = ebaySearchForm()
        return render(request, 'ebay.html', {'form': form})

    def post(self, request):
        form = ebaySearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = ebaySearchForm()
            #return redirect(contact)
            products = search(text)
            context = {"oneProduct" : products, 'form': form, 'text': text}
        return render(request, 'ebay.html', context)



"""
def searchResults(request):
    products = search(self.text)
    context = {
    "oneProduct" : products
        }
    template = 'home.html'
    return render(request, template, context)
"""

class HomeView(TemplateView):
    def get(self, request):
        form = ebaySearchForm()
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        form = ebaySearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = ebaySearchForm()
            #return redirect(contact)
            products = twitterRating(text)
            context = {"oneProduct" : products, 'form': form, 'text': text}
        return render(request, 'home.html', context)

"""
def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)
"""
def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)

def contact(request):
    context = locals()
    template = 'contact.html'
    return render(request, template, context)

def amazon(request):
    context = locals()
    template = 'amazon.html'
    return render(request, template, context)
