from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """serialize the user object"""

    class Meta:
        model = get_user_model()
        fields = ('email','password','name')
        
        #extra kwargs to have extra functionality
        extra_kwargs = {'password':{'write_only':True, 'min_length':4 }}

    # here validated data comes from Meta that comes from request body of request
    def create(self, validated_data):
        """Create the new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)    