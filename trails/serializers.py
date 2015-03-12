from django.contrib.auth.models import User
from rest_framework import serializers

from models import Trail

class TrailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = Trail
		fields = ('id', 'name', 'zip_code', 'distance', 'difficulty', 'elevation_gain',
			'time_required', 'trail_type', 'url', 'city', 'peak_elevation', 'other')
