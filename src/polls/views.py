from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import HomeForm
# Create your views here.
from polls.templatetags.ebayFindingApi import *

class HomeView(TemplateView):
    def get(self, request):
        form = HomeForm()
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
            #return redirect(contact)
            products = search(text)
            context = {"oneProduct" : products, 'form': form, 'text': text}
        return render(request, 'home.html', context)

def searchResults(request):
    products = search(self.text)
    context = {
    "oneProduct" : products
        }
    template = 'home.html'
    return render(request, template, context)

def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)

def contact(request):
    context = locals()
    template = 'contact.html'
    return render(request, template, context)
