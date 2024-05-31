# # # register api

# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


# # # login api

# class LoginSerializer(serializers.Serializer):
#     user_name = serializers.CharField()
#     user_password = serializers.CharField()

# ##########################################################


# # register api

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# # login api

class LoginSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    user_password = serializers.CharField()
    

# # Town api

from .models import Town

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ['town_id', 'town_name']


# # Booth api

from .models import Booth
class BoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = ['booth_id', 'booth_name']
