from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class AppAdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_ad'
    verbose_name = gettext_lazy('Объявления')
