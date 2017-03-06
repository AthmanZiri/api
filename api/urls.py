from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewSet, UserViewSet, api_root
from rest_framework import renderers


post_list = PostViewSet.as_view({
	'get': 'list',
	'post': 'create'
	})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
	})

user_list = UserViewSet.as_view({
    'get': 'list'
	})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
		})