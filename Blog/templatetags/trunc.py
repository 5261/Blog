from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

readMoreSeparator = "<!--more-->"

@register.filter(name = "trunc")
@stringfilter
def trunc(src):
    i = src.find(readMoreSeparator)
    if i != -1:
        return src[:i]
    else:
        return src