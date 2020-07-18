from django import forms

class ebaySearchForm(forms.Form):
    post = forms.CharField(widget = forms.TextInput(
          attrs = {
          'class': 'form-control',
          'placeholder': 'Search ebay',
          }
    ))
