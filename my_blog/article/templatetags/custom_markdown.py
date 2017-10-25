import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()

# @ 符号开始的代码不注释
@register.filter(is_safe=True) #注册template filter
@stringfilter

def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
           extensions = ['markdown.extensions.fenced_code','markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))