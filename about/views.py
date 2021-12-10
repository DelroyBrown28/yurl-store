from django.shortcuts import render
from page_customisations.models import AboutPageCustomisation


def about(request):
    """Returns the about page."""
    about_page_customisation = AboutPageCustomisation.objects.all()
    context = {
        'about_page_customisation' : about_page_customisation,
    }
    return render(request, 'about/about.html', context)

