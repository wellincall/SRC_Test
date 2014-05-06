from __future__ import division
from django import template

register = template.Library()

@register.simple_tag
def percentage(value, total):
	return "{0:.2f}".format(100*value/total)

@register.simple_tag
def format_date(date):
	return date.strftime("%B %d, %Y")