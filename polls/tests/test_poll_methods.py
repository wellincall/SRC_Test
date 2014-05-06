
import datetime
from django.utils import timezone
from django.test import TestCase
from polls.models import Poll

class PollMethodTest(TestCase):
	def test_was_published_recently_with_future_publication_date(self):
		future_poll = Poll(publication_date = timezone.now() + datetime.timedelta(days = 30))
		self.assertEqual(future_poll.was_published_recently(), False)

	def test_was_published_recently_with_past_publication_date(self):
		recent_poll = Poll(publication_date = timezone.now() - datetime.timedelta(hours = 1))
		self.assertEqual(recent_poll.was_published_recently(), True)

	def test_was_published_recently_with_old_publication_date(self):
		old_poll = Poll(publication_date = timezone.now() - datetime.timedelta(days = 30))
		self.assertEqual(old_poll.was_published_recently(), False)