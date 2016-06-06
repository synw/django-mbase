# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(needs_autoescape=True)
@stringfilter
def in_admin(path, autoescape=True):
    if path.startswith("/admin"):
        return True
    return False