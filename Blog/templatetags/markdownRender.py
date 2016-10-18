from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from mistune import markdown

register = template.Library()

@register.filter(name = "markdownRender", is_safe = True)
@stringfilter
def renderMarkdown(src):
    return mark_safe(markdown(src, parse_block_html = True))
