from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig

class MbaseConfig(AppConfig):
    name = "mbase"
    verbose_name = _(u"Mbase")
    
    def ready(self):
        pass