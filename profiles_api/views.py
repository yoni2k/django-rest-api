from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #list of handy http status codes
from profiles_api import serializers
from rest_framework import viewsets

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

    def list(self, request):
        """ List all objects """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality wiht less code',
        ]
        return Response({'message':'Hello!', 'a_viewset' : a_viewset})
