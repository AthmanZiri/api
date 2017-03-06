from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer, UserSerializer
#from blog.serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import filters


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
		})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	filter_backend = (filters.DjangoFilterBackend, filters.OrderingFilter,)
	filter_fields = ('category', 'location', )
	ordering = ('-created', )
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
