from django.shortcuts import render
from django.http import HttpResponseRedirect
from page_customisations.models import TestimonialsPageCustomisation
from .forms import CustomerTestimonialForm


def testimonials(request):
    """Returns the Testimonials page."""

    testimonials = TestimonialsPageCustomisation.objects.all()

    submitted = False
    if request.method == 'POST':
        form = CustomerTestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/testimonials?submitted=True')
    else:
        form = CustomerTestimonialForm()
        if 'submitted' in request.GET:
            submitted = True

    
    return render(request, 'testimonials/testimonials.html', {
        'testimonials': testimonials,
        'form': form,
        'submitted': submitted,
    })
