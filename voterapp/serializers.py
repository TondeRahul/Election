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