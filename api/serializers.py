from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	image1 = serializers.ImageField(max_length=None, use_url=True)
	image2 = serializers.ImageField(max_length=None, use_url=True)
	image3 = serializers.ImageField(max_length=None, use_url=True)

	class Meta:
		model = Post
		fields = ('url', 'id', 'owner', 'title', 'description', 'category', 'price', 'image1', 'image2', 'image3', 
			'location', 'created')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts')