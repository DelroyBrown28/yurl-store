
# from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import TextInput
from products.widgets import CustomClearableFileInput
from .models import Testimonial
from django import forms


class CustomerTestimonialForm(ModelForm):
    class Meta:

        model = Testimonial
        labels = {
            'name': '',
            'email': '',
            'your_thoughts': 'Tell us what you thought of the service.',
            'rating': '',
        }
        fields = (
            'name',
            'email',
            'your_thoughts',
            'rating',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-12', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control col-md-12', 'placeholder': 'Email'}),
            'your_thoughts': forms.Textarea(attrs={'class': 'form-control col-md-12', 'placeholder': 'Your Thoughts?'}),
            'rating': forms.TextInput(attrs={'type': 'number', 'class': 'form-control col-md-3 rating-field', 'placeholder': 'Rate us out of 5'}),
            # 'rating': forms.TextInput(attrs={'class': 'form-control col-md-1', 'placeholder': 'Rating'}),

        }
