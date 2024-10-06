from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# Tags

@register.filter(name = "first_value")
@stringfilter
def first_value(value):
    return value[1]

# Balises

@register.simple_tag
def hello_world(value):
    return f"Hello {value}"