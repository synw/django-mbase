# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

default_statuses =  [
                     (0, _(u'Published')),
                     (1, _(u'Pending')),
                     (2, _(u'Unpublished')),
                     ]

STATUSES = getattr(settings, 'MBASE_STATUSES', default_statuses)
SLUG_MAX_LENGTH = getattr(settings, 'MBASE_SLUG_MAX_LENGTH', 25)
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)