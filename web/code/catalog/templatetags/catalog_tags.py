from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def color_chip(co):
    # {{ hexValue|color_chip:"The Label" }}

    obj = json.loads(co.replace("'", '"'))
    label = obj['color_obj__name']
    hex_code = obj['color_obj__hex_code']
    sortorder = obj['color_obj__sortorder']
    textcolor = "ffffff" if int(sortorder[3:]) < 50 else "000000"
    rv = "".join([
        '<div class="color-chip">',
        '<div class="color-chip__color" style="background-color:#{}">'.format(hex_code),
        # '<img src="http://placehold.it/124x42/{}/{}?text={}" />'.format(
        #     hex_code, textcolor, label.upper()),
        '<img src="http://placehold.it/110x50/{}/{}?text={}" />'.format(
            hex_code, hex_code, label.upper()),
        '</div><div class="color-chip__info">',
        '<div class="color-chip__info__title">{}</div></div></div>'.format(label)
    ])

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
