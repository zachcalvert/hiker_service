from django.conf.urls import patterns, include, url
from rest_framework import routers

import views

router = routers.DefaultRouter()
router.register(r'^trails', views.EntryViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
)
