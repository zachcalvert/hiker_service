from decimal import Decimal

from django.db import models

class Trail(models.Model):
	"""
	A simple model providing info about a trail
	"""
	name = models.CharField(max_length=100)
	distance = models.DecimalField(max_digits=5, decimal_places=1, default=Decimal('0.0'))
	difficulty = models.CharField(u'Difficulty', max_length=100, default='easy')
	elevation_gain = models.CharField(max_length=20, default='minimal')
	time_required = models.CharField(max_length=50, default='minimal')
	zip_code = models.IntegerField(default=97202)
	trail_type = models.CharField(max_length=30, null=True, blank=True)
	url = models.URLField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=30, null=True, blank=True)
	peak_elevation = models.CharField(max_length=30, null=True, blank=True)
	other = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name
