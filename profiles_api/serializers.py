from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    #the way to use ModelSerializer is to create a Meta class to configure ModelSerializer to work with specific model
    class Meta:
        model = models.UserProfile #model we defined
        fields = ('id', 'email', 'name', 'password') #list of fields accessible in the model by the serializer
        extra_kwargs = {
            'password' : {  #field we want to give extra configuration argument
                'write_only': True,  #can only be used to create new object or update objects, not retrieve
                'style': {'input_type':'password'} #to make input with *** instead of clear text passwords
            }
        }


    def create(self, validated_data):
        """ Create and return a new user """
        #overrides the default create function of ModelSerializer that wouldn't hash the password
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password=validated_data['password']
        )

        return user
