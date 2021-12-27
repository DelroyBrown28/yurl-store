from page_customisations.models import ProductsPageCustomisation, CTACard, ProductBanner
from products.models import Category, Product
from testimonials.models import Testimonial
from page_customisations.views import (HeaderCustomisation,
                                       ProductsPageCustomisation,
                                       GlobalSiteStyling,
                                       FooterCustomisation,
                                       TestimonialsPageCustomisation,
                                       AddTestimonial)
from home.views import HomePage_Customisation


def global_styles_processor(request):
    return {
        'global_styles': GlobalSiteStyling.objects.all(),
    }

# Home Page Processor


def home_page_styles_processor(request):
    return {
        'home_page_styles': HomePage_Customisation.objects.all(),
    }
# Home Page Processor


def header_customisation_processor(request):
    return {
        'header_customisation': HeaderCustomisation.objects.all(),

    }


def cta_processor(request):
    return {
        'cta_customisation': CTACard.objects.all(),

    }


def product_banner_processor(request):
    return {
        'product_banner_customisation': ProductBanner.objects.all(),

    }


def categories_processor(request):
    return {
        'categories_processor': Category.objects.all(),

    }


def products_processor(request):
    return {
        'products_processor': Product.objects.all(),

    }


def footer_customisation_processor(request):
    return {
        'footer_customisation': FooterCustomisation.objects.all(),

    }


def testimonials_customisation_processor(request):
    return {
        'testimonials_customisation': TestimonialsPageCustomisation.objects.all(),

    }


def testimonials_push(request):
    return {
        'testimonials_push': Testimonial.objects.all(),

    }


def add_testimonial_processor(request):
    return {
        'add_testimonial': AddTestimonial.objects.all(),

    }


def products_page_customisation_processor(request):
    return {
        'products_page_customisation': ProductsPageCustomisation.objects.all(),
    }
