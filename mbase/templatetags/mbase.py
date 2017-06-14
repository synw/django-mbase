# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(needs_autoescape=True)
@stringfilter
def in_admin(path, autoescape=True):
    if path.startswith("/admin"):
        return True
    return False

@register.filter
def is_installed(vvapp):
    if vvapp in settings.INSTALLED_APPS:
        return True
    return False
