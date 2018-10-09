from cms.models import CMSPlugin
from django.db import models
from mypolls.models import Poll


class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Poll)

    def __unicode__(self):
        return self.poll.question
