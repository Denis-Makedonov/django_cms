from django.db import models
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    question = models.CharField(_('Question'), max_length=200)

    class Meta:
        verbose_name = _('poll')
        verbose_name_plural = _('polls')

    def __str__(self):              # Python 3: def __unicode__(self):
        return self.question


class Choice(models.Model):
    choice_text = models.CharField(_('Choice content'), max_length=200)

    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll)

    class Meta:
        verbose_name = _('choice')
        verbose_name_plural = _('choices')

    def __str__(self):              # Python 3: def __unicode__(self):
        return self.choice_text
