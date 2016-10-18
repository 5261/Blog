from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

register = template.Library()

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall = True)
        formatter = html.HtmlFormatter(style = "monokai")
        return highlight(code, lexer, formatter)

renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer = renderer)

@register.filter(name = "markdownRender", is_safe = True)
@stringfilter
def renderMarkdown(src):
    return mark_safe(markdown(src))
