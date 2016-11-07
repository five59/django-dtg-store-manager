from django import template
# from printaura.models import *

register = template.Library()

@register.inclusion_tag('master/tag_navbar.html', takes_context=True)
def draw_navbar(context):
    return {
        # 'lpgs': LocalProductGroup.objects.all(),
        # 'brands': Brand.objects.all(),
    }
