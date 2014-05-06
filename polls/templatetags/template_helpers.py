from __future__ import division
from django import template

register = template.Library()

@register.simple_tag
def percentage(value, total):
	return "{0:.2f}".format(100*value/total)
