from django.contrib import admin
from polls.models import Poll, Choice

#Defining inline items
class ChoiceInLine(admin.StackedInline):
	model = Choice
	extra = 0

#Defining administrative view
class PollAdmin(admin.ModelAdmin):
	list_display = ('question', 'publication_date', 'was_published_recently')
	fields = ["publication_date","question"]
	inlines = [ChoiceInLine]
	list_filter = ["publication_date"]
	search_fields = ["question"]


#registering view
admin.site.register(Poll, PollAdmin)