import django_filters
from rest_framework import viewsets
from rest_framework import filters
from django.views import generic

from models import Trail
from serializers import TrailSerializer

class TrailFilter(django_filters.FilterSet):
	min_distance = django_filters.NumberFilter(name='distance', lookup_type='gte')
	max_distance = django_filters.NumberFilter(name='distance', lookup_type='lte')

	class Meta:
		model = Trail
		fields = ['zip_code', 'city', 'min_distance', 'max_distance']

class EntryViewSet(viewsets.ModelViewSet):
	queryset = Trail.objects.all()
	serializer_class = TrailSerializer
	filter_class = TrailFilter

	def pre_save(self, obj):
		obj.owner = self.request.user
