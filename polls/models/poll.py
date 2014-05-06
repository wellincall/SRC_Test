from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Poll(models.Model):
	class Meta:
		app_label = "polls"

	#Class attributes
	question = models.CharField(max_length = 256)
	publication_date = models.DateTimeField('date published')
	#end Class attributes
	def __unicode__(self):
		return self.question
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days = 1) <= self.publication_date < now
	was_published_recently.boolean = True
	was_published_recently.short_description = "Published recently?"
	was_published_recently.admin_order_field = "publication_date"
	def total_votes(self):
		total_votes = None
		if not total_votes: 
			total_votes = 0
			for choice in self.choice_set.all():
				total_votes += choice.votes
		return total_votes