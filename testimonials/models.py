from django.db import models



class Testimonial(models.Model):
    """
    This model is for the customers on the frontend.
    And also in the admin
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    your_thoughts = models.TextField(max_length=350, blank=False, null=False)
    rating = models.CharField(max_length=1, null=True, blank=True)
    date_received = models.DateTimeField(auto_now_add=True)
    push_to_testimonial_page = models.BooleanField(default=False)

    def __str__(self):
        return f"Customer testimonial from {self.name}"
