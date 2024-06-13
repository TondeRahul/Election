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


from rest_framework import serializers
from .models import Voterlist

class VoterlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voterlist
        fields = '__all__'


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


# # Panchayat_samiti api

from .models import PanchayatSamiti

class PanchayatSamitiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanchayatSamiti
        fields = ['panchayat_samiti_id', 'panchayat_samiti_name']


# # ZP api

from .models import ZP

class ZPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZP
        fields = ['zp_id', 'zp_name']


# # Vidhansabha api 

from .models import Vidhansabha

class VidhansabhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vidhansabha
        fields = ['vidhansabha_id', 'vidhansabha_name']


# # State api

from .models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['state_id', 'state_name']
