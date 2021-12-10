from django.shortcuts import render
from testimonials.models import Testimonial
from .models import (AddTestimonial, HeaderCustomisation,
                     ProductsPageCustomisation,
                     GlobalSiteStyling,
                     FooterCustomisation,
                     TestimonialsPageCustomisation)


def header_customisation(request):
    """Customisation for header contents"""
    header_customisation = TestimonialsPageCustomisation.objects.all()
    context = {
        'header_customisation': header_customisation,
    }
    return render(request, 'includes/header.html', context)


def products_page_customisation(request):
    """Customisation for products page"""
    products_page_customisation = ProductsPageCustomisation.objects.all()
    context = {
        'products_page_customisation': products_page_customisation,
    }
    return render(request, 'products/products.html', context)


def add_testimonial(request):
    """Customisation for products page"""
    add_testimonial = AddTestimonial.objects.all()
    context = {
        'add_testimonial': add_testimonial,
    }
    return render(request, 'products/products.html', context)

def push_testimonial(request):
    """Customisation for products page"""
    push_testimonial = Testimonial.objects.all()
    context = {
        'push_testimonial': push_testimonial,
    }
    return render(request, 'testimonials/testimonials.html', context)


def footer_customisation(request):
    """Customisation for products page"""
    footer_customisation = FooterCustomisation.objects.all()
    context = {
        'footer_customisation': footer_customisation,
    }
    return render(request, 'products/footer.html', context)


def global_site_styles(request):
    """Customisation for all pages"""
    global_site_styles = GlobalSiteStyling.objects.all()
    context = {
        'global_site_styles': global_site_styles,
    }
    return render(request, 'products/products.html', context)
