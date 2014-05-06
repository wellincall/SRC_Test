from django.db import models
import datetime
from django.utils import timezone
from polls.models import Poll

class Choice(models.Model):
	class Meta:
		app_label = "polls"

	#class attributes
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length = 256)
	votes = models.IntegerField(default = 0)
	#end class attributes
	def __unicode__(self):
		return self.choice_text