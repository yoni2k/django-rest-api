from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #list of handy http status codes
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication #for authenticating our users, creates token on login, passes on every request
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """ Test API View of Hello World """
    #configures API view with specific serializer
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        # Response must contain a dictionary or list of what to return, will be converted to JSON
        return Response({'message' : 'Hello!',
                        'an_apiview' : an_apiview})


    def post(self, request, format=None):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        #in our case is_valid checks that the length is <= 10
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            #serializer created the errors list of parsing
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST #by default Response returns 200
            )


    def put(self, request, pk=None):
        """ Handle updating an object """
        #Usually pk is used for an ID of specific item that's being updated
        return Response({'method' : 'PUT'})


    def patch(self, request, pk=None):
        """  Handle patching an object - partial update, update specific fields """
        return Response({'method' : 'PATCH'})


    def delete(self, request, pk=None):
        """  Handle deleting an object """
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    #reusing the same serializer
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """ List all objects """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality wiht less code',
        ]
        return Response({'message':'Hello!', 'a_viewset' : a_viewset})

    def create(self, request):
        """ Create a new hello message """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message', message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handle getting an object by it's ID """
        return Response({'http_method' : 'GET'})


    def update(self, request, pk=None):
        """ Handle updating an object by it's ID """
        return Response({'http_method' : 'PUT'})


    def partial_update(self, request, pk=None):
        """ Handle updating part an object by it's ID """
        return Response({'http_method' : 'PATCH'})


    def destroy(self, request, pk=None):
        """ Handle destoying an object by it's ID """
        return Response({'http_method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet): #ModelViewSet is similar to ViewSet with additional model functionality
    """ Handle creating and updating user profiles """
    serializer_class = serializers.UserProfileSerializer

    #ModelViewSet will add on it's own all actions provided by model and serializer
    queryset = models.UserProfile.objects.all()

    #add to check user authentication with token against the action the user is doing
    authentication_classes = (TokenAuthentication,) #see token explanation in imports
    permission_classes = (permissions.UpdateOwnProfile,)

    # adding ability to filter (by built in SearchFilter)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',) #search for a string in these fields

class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentiation tokens """
    #render it in all default views, by default other views add it, but ObtainAuthToken doesn't
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading and updating profile feed items """
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,) #see token explanation in imports
    queryset = models.ProfileFeedItem.objects.all() #all fields/objects will be managed
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly, #will make sure user must be authenticated
    )

    # overridding allows override/customize behavior of creating objects through ModelViewSet
    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user """
        # set the user_profile to be of current requester user
        serializer.save(user_profile=self.request.user)
