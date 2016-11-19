from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def color_chip(hex_code, label):
    # {{ hexValue|color_chip:"The Label" }}

    rv = '<div class="color-chip"><div class="color-chip__color" style="background-color:{}"></div><div class="color-chip__info"><div class="color-chip__info__title">{}</div></div></div>'.format(
        hex_code, label)

    # rv = "<span class='colorchip'><i style='background-color:{};'></i> {}</span>".format(
    #     hex_code, label)
    return mark_safe(rv)


# .color-chip {
#   float: left;
#   margin: 1.5em 1.5em 0 0;
#   height: 20em;
#   width: 12.5em;
#   color: #666;
#   background-color: #fff;
#   border-radius: 3px;
#   box-shadow: 0 1px 1px 0 rgba(#000, .15), 0 1px 2px 0 rgba(#000, .1);
#   transition: box-shadow .3s;
#
#   &:hover {
#     box-shadow: 0px 4px 10px 0 rgba(#000, .1), 0px 2px 10px 0px rgba(#000, .1);
#   }
# }
#
