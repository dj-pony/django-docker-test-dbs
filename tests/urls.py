# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('dj_pony.django_docker_test_dbs.urls', namespace='django_docker_test_dbs')),
]
