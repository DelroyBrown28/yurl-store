from enum import unique
from django.db import models
from django.db.models.fields import CharField, EmailField, TextField
from django.db.models.fields.json import HasKeyLookup
from products.models import Category
from django.utils.html import mark_safe
from djrichtextfield.models import RichTextField
from colorfield.fields import ColorField
from phonenumber_field.modelfields import PhoneNumberField


class GlobalSiteStyling(models.Model):
    SITE_BORDERS = (
        ('action-button-border', 'Add Border'),
        ('no-border-action-button-border', 'No Border'),
    )
    global_site_styles = models.CharField(
        blank=False, null=False, max_length=25, default='Default Global Styles')
    base_background_color = ColorField(format='hex', default='#FFFFFF')
    base_font_color = ColorField(format='hexa', default='#000000')
    all_icon_colors = ColorField(format='hexa', default='#000000')
    action_button_color = ColorField(format='hexa', default='#000000')
    action_button_border = models.TextField(
        choices=SITE_BORDERS, blank=False, null=False, default='no-border-action-button-border')
    action_button_border_color = ColorField(format='hexa', default='#000000')
    action_button_text_color = ColorField(format='hexa', default='#000000')
    secondary_button_color = ColorField(format='hexa', default='#FFFFFF')
    secondary_button_text_color = ColorField(format='hexa', default='#000000')
    secondary_button_border = models.TextField(
        choices=SITE_BORDERS, blank=False, null=False, default='no-border-action-button-border')
    secondary_button_border_color = ColorField(format='hexa', default='#000000')
    pop_up_background_color = ColorField(format='hexa', default='#FFFFFF')
    pop_up_text_color = ColorField(format='hexa', default='#000000')
    dropdown_menu_background_color = ColorField(
        format='hexa', default='#FFFFFF')
    dropdown_menu_text_color = ColorField(format='hexa', default='#000000')

    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='Check this box to hide this specific styling.')

    class Meta:
        verbose_name_plural = '        Global Page Styles'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = GlobalSiteStyling.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except GlobalSiteStyling.DoesNotExist:
                pass
        super(GlobalSiteStyling, self).save(*args, **kwargs)

    def __str__(self):
        return self.global_site_styles


class CTACard(models.Model):
    ADD_BUTTON_BORDER = (
        ('add-border', 'Add Border'),
        ('no-border', 'Remove Border'),
    )
    cta_title = models.CharField(
        blank=False, null=False, max_length=100, default="Default CTA Card Styling.")
    image = models.ImageField(null=False, blank=False,
                              upload_to='cta_card_images')
    cta_text = RichTextField()
    cta_text_color = ColorField(format='hexa', default='#000000')
    button_url_choice = models.ForeignKey('products.Category', null=True, blank=True, related_name='button_url',
                                          on_delete=models.CASCADE, help_text="Connect to one of your categories")
    button_label = models.CharField(max_length=25, blank=False, null=False)
    button_background_color = ColorField(format='hexa', default='#000000')
    button_label_color = ColorField(format='hexa', default='#FFFFFF')
    add_button_border = models.TextField(choices=ADD_BUTTON_BORDER,
                                         blank=False,
                                         null=False,
                                         default="no-border")
    border_color = ColorField(format='hexa', default='#000000')

    def __str__(self):
        return self.cta_title


class ProductBanner(models.Model):
    ADD_BUTTON_BORDER = (
        ('add-border', 'Add Border'),
        ('no-border', 'Remove Border'),
    )
    banner_title = models.CharField(
        max_length=25, blank=False, null=False, default='Default Banner Styles')
    banner_background_color = ColorField(format='hexa', default='#000000')
    banner_image = models.ImageField(blank=True, null=True, upload_to='banner_images',
                                     help_text='You can have a banner image or a banner image color.')
    product_banner_title = RichTextField(default="")
    product_banner_blurb = RichTextField(default="")
    cta_button_label = models.CharField(
        max_length=25, null=False, blank=False, default="")
    label_color = ColorField(format='hexa', default='#000000')
    add_button_border = models.TextField(
        choices=ADD_BUTTON_BORDER, blank=False, null=False, default='no-border')
    border_color = ColorField(format='hexa', default='#000000')
    # TODO: Give option of internal URL or external URL
    button_background_color = ColorField(format='hexa', default='#FFFFFF')
    product_card_title_color = ColorField(format='hexa', default='#000000')
    product_card_button_text = models.CharField(blank=False, null=False, max_length=25, default='View Product')
    card_button_background_color = ColorField(format='hexa', default='#000000')
    product_card_button_text_color = ColorField(format='hexa', default='#000000')
    button_border = models.TextField(
        choices=ADD_BUTTON_BORDER, blank=False, null=False, default='no-border')
    button_border_color = ColorField(format='hexa', default='#000000')
    cta_button_url = models.URLField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.banner_title


class HomePageCustomisation(models.Model):
    TEXT_ALIGNMENT_CHOICES = {
        ('text-align__right', 'Right'),
        ('text-align__left', 'Left'),
        ('text-align__center', 'Center'),
    }
    BUTTON_ALIGNMENT_CHOICES = {
        ('text-align__right', 'Right'),
        ('text-align__left', 'Left'),
        ('text-align__center', 'Center'),
    }
    home_page_styling = models.CharField(
        blank=False, null=False, max_length=100, default="Default Home Page Styling")
    image = models.ImageField(null=True, blank=True,
                              upload_to='home_page_images')
    main_page_text = RichTextField()
    main_page_text_alignment = models.TextField(
        choices=TEXT_ALIGNMENT_CHOICES, blank=False, null=False, default='text-align__left')
    main_page_text_color = ColorField(format='hexa')
    button_text = models.CharField(
        blank=False, null=False, max_length=15, default='Shop Now')
    button_text_color = ColorField(format='hexa')
    button_background_color = ColorField(format='hexa')
    main_page_button_alignment = models.TextField(
        choices=BUTTON_ALIGNMENT_CHOICES, blank=False, null=False, default='text-align__left')
    cta_card_1 = models.ForeignKey(
        'CTACard', null=True, blank=True, related_name='cta_card_1', on_delete=models.CASCADE, help_text='Click the + button to create a new CTA card.')
    cta_card_2 = models.ForeignKey(
        'CTACard', null=True, blank=True, related_name='cta_card_2', on_delete=models.CASCADE, help_text='Click the + button to create a new CTA card.')
    product_banner = models.ForeignKey(
        'ProductBanner', null=True, blank=True, related_name='cta_banner', on_delete=models.CASCADE, help_text='Click the + button to create a new CTA banner.')
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='CHECK THIS BOX TO HIDE THIS SPECIFIC STYLING.')

    class Meta:
        verbose_name_plural = '     Home Page'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = HomePageCustomisation.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except HomePageCustomisation.DoesNotExist:
                pass
        super(HomePageCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.home_page_styling


class HeaderCustomisation(models.Model):
    ADD_BUTTON_BORDER = (
        ('add-border', 'Add Border'),
        ('no-border', 'Remove Border'),
    )
    header_styling = models.CharField(
        blank=False, null=False, max_length=55, default="Default Header Styling")
    header_logo = models.ImageField(null=True, blank=True, upload_to='media')
    header_background_color = ColorField(format='hexa')
    search_icon_color = ColorField(format='hexa')
    search_icon_background_color = ColorField(format='hexa')
    small_banner_text = RichTextField()
    small_banner_background_color = ColorField(format='hexa')
    small_banner_text_color = ColorField(format='hexa')
    banner_button_label_1 = models.CharField(
        default='', blank=True, null=True, max_length=25)
    banner_button_url_link_1 = models.URLField(
        blank=True, null=True, max_length=250)
    banner_button_label_2 = models.CharField(
        default='', blank=True, null=True, max_length=25)
    banner_button_url_link_2 = models.URLField(
        blank=True, null=True, max_length=250)
    banner_button_background_color = ColorField(
        format='hexa', default='#FFFFFF')
    banner_button_label_color = ColorField(format='hexa', default='#000000')
    button_border = models.TextField(
        choices=ADD_BUTTON_BORDER, null=True, blank=True, default='no-border')
    button_border_color = ColorField(format='hexa', default='#000000')
    edit_banner_buttons = models.CharField(
        max_length=120, null=True, blank=True, default='/superadmin/page_customisations/headercustomisation/1/change/')
    id_tag = models.AutoField(primary_key=True, unique=True)
    mobile_banner_button_background_color = ColorField(
        format='hexa', default='#FFFFFF')
    mobile_banner_button_label_color = ColorField(
        format='hexa', default='#000000')
    mobile_button_border = models.TextField(
        choices=ADD_BUTTON_BORDER, null=True, blank=True, default='no-border')
    mobile_button_border_color = ColorField(format='hexa', default='#000000')
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='CHECK THIS BOX TO HIDE THIS SPECIFIC STYLING.')

    class Meta:
        verbose_name_plural = '      Header'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = HeaderCustomisation.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except HeaderCustomisation.DoesNotExist:
                pass
        super(HeaderCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.header_styling


class ProductsPageCustomisation(models.Model):
    ADD_PRODUCT_CARD_BORDER = (
        ('add-product-card-border', 'Add Border'),
        ('no-border-product-card', 'No Border'),
    )
    products_page_styling = models.CharField(
        blank=False, null=False, max_length=55, default="Default Product Page Styling")
    category_tag_border_color = ColorField(format='hexa', default='#000000')
    category_tag_text_color = ColorField(format='hexa', default='#000000')
    product_card_background_color = ColorField(
        format='hexa', default='#FFFFFF00')
    add_card_border = models.TextField(choices=ADD_PRODUCT_CARD_BORDER,
                                       blank=False,
                                       null=False,
                                       default="no-border")
    border_color = ColorField(format='hexa', default='#000000')
    product_card_font_color = ColorField(format='hex', default='#000000')
    product_card_icon_color = ColorField(format='hexa', default='#000000')
    product_quantity_button_background_color = ColorField(
        format='hexa', default='#000000')
    product_quantity_button_icon_color = ColorField(
        format='hexa', default='#FFFFFF')
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='**Check this box to hide this specific styling.')

    class Meta:
        verbose_name_plural = '    Products Page'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = ProductsPageCustomisation.objects.get(
                    do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except ProductsPageCustomisation.DoesNotExist:
                pass
        super(ProductsPageCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.products_page_styling


class AboutPageCustomisation(models.Model):
    ADD_BORDER = (
        ('add-contact-card-border', 'Add Border'),
        ('no-border', 'No Border'),
    )
    styling_name = models.CharField(
        blank=False, null=False, max_length=55, default="Default")
    about_page_title = models.CharField(
        max_length=100, blank=False, null=False)
    about_page_blurb = RichTextField()
    story_of_your_brand = RichTextField()
    about_page_left_image = models.ImageField(
        null=True, blank=True, upload_to='about_page_images')
    about_page_right_image = models.ImageField(
        null=True, blank=True, upload_to='about_page_images')
    contact_section_title = models.CharField(
        max_length=100, blank=False, null=False)
    contact_section_blurb = RichTextField(default='')
    contact_card_title = models.CharField(
        max_length=100, blank=False, null=False, default='Business Name')
    contact_card_info = RichTextField()
    contact_card_image = models.ImageField(
        null=True, blank=True, upload_to='about_page_images/contact_page_images')
    contact_card_background_color = ColorField(format='hex', default='#FFFFFF')
    contact_card_text_color = ColorField(format='hex', default='#00000')
    contact_card_border = models.TextField(choices=ADD_BORDER,
                                           blank=False,
                                           null=False,
                                           default="no-border")
    border_color = ColorField(format='hexa')

    twitter_link = models.URLField(
        max_length=200, null=True, blank=True, default='')
    linkedin_link = models.URLField(
        max_length=200, null=True, blank=True, default='/')
    facebook_link = models.URLField(
        max_length=200, null=True, blank=True, default='')
    instagram_link = models.URLField(
        max_length=200, null=True, blank=True, default='')

    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='**Check this box to hide this specific styling.')

    class Meta:
        verbose_name_plural = '  About Page'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = AboutPageCustomisation.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except AboutPageCustomisation.DoesNotExist:
                pass
        super(AboutPageCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.styling_name


class TestimonialsPageCustomisation(models.Model):
    """
    This model is to custmoise the testimonial page
    """
    TESTIMONIAL_CARD_BORDER = (
        ('add-border', 'Add Border'),
        ('no-border', 'No Border'),
    )
    TESTIMONIAL_FORM_FIELD_BORDERS = (
        ('bottom-border', 'Bottom Border'),
        ('full-border', 'Full Border'),
        ('no-border', 'No Border'),
    )
    style_name = models.CharField(
        blank=False, null=False, max_length=100, default='Default')
    card_background_color = ColorField(
        format='hexa', blank=True, null=True, default='#FFFFFF')
    card_border = models.TextField(
        choices=TESTIMONIAL_CARD_BORDER, blank=True, null=True, default='no-border')
    card_border_color = ColorField(
        format='hexa', blank=True, null=True, default='#000000')
    card_font_color = ColorField(
        format='hexa', blank=True, null=True, default='#000000')
    star_rating_color = ColorField(
        format='hexa', blank=True, null=True, default='#FFE231')
    drop_to_form_label = models.CharField(
        blank=False, null=False, max_length=55, default='', help_text='Button that drops you down to the Testimonials Form')
    drop_to_form_label_color = ColorField(
        format='hexa', default='#000000')
    drop_to_form_background_color = ColorField(
        format='hexa', default='#FFFFFF')
    drop_to_form_border = models.TextField(
        choices=TESTIMONIAL_CARD_BORDER, blank=True, null=True, default='no-border')
    drop_to_form_border_color = ColorField(
        format='hexa', default='#000000')
    icon_color = ColorField(format='hexa', default='#000000')
    form_title = RichTextField(blank=True, null=True, max_length=300, default='', field_settings={'bold': False})
    testimonial_form_blurb = RichTextField(
        blank=True, null=True, max_length=250, default='')
    form_background_color = ColorField(
        format='hexa', blank=True, null=True,  default='#FFFFFF')
    form_font_color = ColorField(
        format='hexa', blank=True, null=True,  default='#00000')
    form_field_borders = models.TextField(
        choices=TESTIMONIAL_FORM_FIELD_BORDERS, blank=True, null=True, default='no-border')
    form_field_border_color = ColorField(
        format='hexa', blank=True, null=True, default='#000000')
    form_field_background_color = ColorField(
        format='hexa', blank=True, null=True, default='#FFFFFF')
    form_field_placeholder_color = ColorField(
        format='hexa', blank=True, null=True, default='#000000')
    form_field_text_color = ColorField(
        format='hexa', blank=True, null=True, default='#000000')
    submit_button_border_color = ColorField(
        format='hexa', blank=True, null=True,  default='#000000')
    submit_button_background_color = ColorField(
        format='hexa', blank=True, null=True,  default='#FFFFFF')
    submit_button_label = CharField(
        blank=False, null=False, default='', max_length=25)
    submit_button_label_color = ColorField(
        format='hexa', blank=True, null=True,  default='#000000')
    add_button_border = TextField(
        choices=TESTIMONIAL_CARD_BORDER, blank=True, null=True, default='no-border')
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='**Check this box to hide this specific styling.')

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = TestimonialsPageCustomisation.objects.get(
                    do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except TestimonialsPageCustomisation.DoesNotExist:
                pass
        super(TestimonialsPageCustomisation, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '  Testimonials Page'

    def __str__(self):
        return self.style_name


class AddTestimonial(models.Model):
    recipients_name = models.CharField(max_length=100, blank=False, null=False)
    testimonial = RichTextField(blank=False, null=False, max_length=500)
    customers_rating = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        verbose_name_plural = ' Add Testimonial'

    def __str__(self):
        return self.recipients_name


class FooterCustomisation(models.Model):
    styling_name = models.CharField(
        blank=False, null=False, max_length=55, default="Default Footer Styles")
    background_color = ColorField(format='hexa', default='#000000')
    footer_logo = models.ImageField(
        null=True, blank=True, upload_to='footer_logo_images')
    footer_top_border_color = ColorField(format='hexa', default='#000000')
    footer_title_colors = ColorField(format='hexa', default='#000000')
    footer_text_color = ColorField(format='hexa', default='#000000')
    footer_icon_colors = ColorField(format='hexa', default='#FFFFFF')

    twitter_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://twitter.com/')
    linkedin_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://linkedin.com/')
    facebook_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://facebook.com/')
    instagram_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://instagram.com/')

    social_media_icon_background_color = ColorField(format='hexa', default='#000000')
    social_media_icon_colors = ColorField(format='hexa', default='FFFFFF')
    email = models.EmailField(
        null=True, blank=True, help_text='Enter your email to be displayed in the footer.')
    contact_number = PhoneNumberField(
        null=True, blank=True, help_text='Enter your contact number to be displayed in the footer.')

    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='**Check this box to hide this specific styling.')

    class Meta:
        verbose_name_plural = ' Footer'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = FooterCustomisation.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except FooterCustomisation.DoesNotExist:
                pass
        super(FooterCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.styling_name
