NUEUI

sdsadasdsad




   <div {% if user.is_superuser %} data-bs-toggle="tooltip"
    data-bs-placement="bottom" title="Double click to edit small banner" {% endif %}  class="{% if x.do_not_display or y.do_not_display %}
     do-not-display {% else %} row text-center flexed editable small-banner-wrap {% endif %}" data-aos="fade-in"
        data-aos-delay="1000" style="background-color: {{ x.small_banner_background_color }};">

        <a {% if user.is_superuser %} data-bs-toggle="tooltip" data-bs-placement="bottom"
        title="Double click to edit small banner buttons" {% else %} href="{{ x.banner_button_url_link_1 }}"  {% endif %} target="_blank" class="{% if x.do_not_display or y.do_not_display  %}
        do-not-display {% else %} small-banner-btns flexed {{ x.button_border }} {% endif %}" style="background-color: {{ x.banner_button_background_color }} !important;
            color: {{ x.banner_button_label_color }} !important;
            border: 2px solid {{ x.button_border_color }} !important;">
            {{ x.banner_button_label_1 }}
        </a>
        <div class="col free-delivery-wrap">
            <!-- <h5 class="free-delivery-text my-1">Free delivery on orders over £{{ free_delivery_threshold }}!</h5> -->
            <h5 class="{% if x.do_not_display or y.do_not_display  %}
            do-not-display {% else %} small-banner-text my-1 py-2 {% endif %}"
                style="color: {{ x.small_banner_text_color }};">
                {{ x.small_banner_text|safe }}
            </h5>

        </div>
        <a {% if user.is_superuser %} ondblclick="editSmallBannerButtons()" data-bs-toggle="tooltip" data-bs-placement="bottom"
        title="Double click to edit small banner buttons" {% else %} href="{{ x.banner_button_url_link_2 }}" {% endif %} target="_blank" class="{% if x.do_not_display or y.do_not_display  %}
        do-not-display {% else %} small-banner-btns flexed {{ x.button_border }} {% endif %}" style="background-color: {{ x.banner_button_background_color }} !important;
            color: {{ x.banner_button_label_color }} !important;
            border: 2px solid {{ x.button_border_color }} !important;">
            {{ x.banner_button_label_2 }}
        </a>

    </div># yurl-store
