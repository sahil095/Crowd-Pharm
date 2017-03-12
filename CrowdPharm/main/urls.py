from django.conf.urls import url

from .views import (
		index,
		input_med,
	)

urlpatterns = [

		url(r'^$',index, name='index'),
		url(r'^create/$',input_med),
]