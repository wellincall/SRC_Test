import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from polls.models import Poll


def create_poll(question_text, deadline_to_be_published):
	return Poll.objects.create(publication_date = timezone.now() + datetime.timedelta(days = deadline_to_be_published), question = question_text)
	
class PollIndexViewTest(TestCase):
	def test_index_with_no_polls(self):
		response = self.client.get(reverse("polls:index"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['lastest_polls'], [])
		self.assertContains(response, "There are no polls registered")


	def test_index_with_a_past_poll(self):
		past_poll = create_poll("This is a past poll.", -3)
		response = self.client.get(reverse("polls:index"))
		self.assertQuerysetEqual(response.context['lastest_polls'],map(repr,[past_poll]))

	def test_index_with_a_future_poll(self):
		future_poll = create_poll("It should not be listed in the screen", 30)
		response = self.client.get(reverse("polls:index"))
		self.assertNotIn(future_poll, response.context['lastest_polls'])
		self.assertContains(response, "There are no polls registered")

	def test_index_with_future_and_past_polls(self):
		past_poll = create_poll("This poll wil be displayed in screen", -9)
		future_poll = create_poll("This poll should not be fetched", 20)
		response = self.client.get(reverse("polls:index"))
		self.assertIn(past_poll, response.context['lastest_polls'])
		self.assertNotIn(future_poll, response.context['lastest_polls'])

	def test_index_with_two_past_polls(self):
		past_poll = create_poll("younger poll",-2)
		older_poll = create_poll("This is the oldest poll", -30)
		response = self.client.get(reverse("polls:index"))
		self.assertIn(past_poll, response.context['lastest_polls'])
		self.assertIn(older_poll, response.context['lastest_polls'])

class PollDetailViewTest(TestCase):
	def test_404_for_future_publication_dates(self):
		future_poll = create_poll("This will throw an error", 30)
		response = self.client.get(reverse("polls:detail", args = (future_poll.id, )))
		self.assertEqual(response.status_code, 404)
		
	def test_allow_voting_for_publication_data_in_the_past(self):
		past_poll = create_poll("You are able to vote", -1)
		response = self.client.get(reverse("polls:detail", args = (past_poll.id, )))
		self.assertEqual(response.context['poll'], past_poll)
		self.assertEqual(response.status_code, 200)