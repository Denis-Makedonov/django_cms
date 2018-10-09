from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MypollsConfig(AppConfig):
    name = 'mypolls'
    verbose_name = _('Polls')
