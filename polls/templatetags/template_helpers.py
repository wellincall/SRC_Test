from __future__ import division
from django import template
from random import randint
register = template.Library()

@register.simple_tag
def percentage(value, total):
	return "{0:.2f}".format(100*value/total)

@register.simple_tag
def format_date(date):
	return date.strftime("%B %d, %Y")

@register.simple_tag
def random_color():	
	color = "#"
	for i in range(6):
		color += hex(randint(0,15))[2].upper()
	return color