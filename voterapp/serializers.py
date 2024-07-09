# # voter api 

# from rest_framework import serializers
# from .models import Voterlist, Town, Booth

# class VoterlistSerializer(serializers.ModelSerializer):
#     town_name = serializers.SerializerMethodField()
#     booth_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Voterlist
#         fields = ['voter_id', 'voter_name', 'voter_parent_name', 'voter_house_number', 'voter_age', 'voter_gender', 'town_name', 'booth_name', 'voter_contact_number', 'voter_cast']

#     def get_town_name(self, obj):
#         try:
#             town = Town.objects.get(town_id=obj.voter_town_id)
#             return town.town_name
#         except Town.DoesNotExist:
#             return None

#     def get_booth_name(self, obj):
#         try:
#             booth = Booth.objects.get(booth_id=obj.voter_booth_id)
#             return booth.booth_name
#         except Booth.DoesNotExist:
#             return None


# # # register api

# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ['user_name', 'user_phone', 'user_password']



# # # login api

# class LoginSerializer(serializers.Serializer):
#     user_name = serializers.CharField()
#     user_password = serializers.CharField()
    

# # # Town api

# from .models import Town

# class TownSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Town
#         fields = ['town_id', 'town_name']


# # # Booth api

# from .models import Booth
# class BoothSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booth
#         fields = ['booth_id', 'booth_name']


# # # Panchayat_samiti api

# from .models import PanchayatSamiti

# class PanchayatSamitiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PanchayatSamiti
#         fields = ['panchayat_samiti_id', 'panchayat_samiti_name']


# # # ZP api

# from .models import ZP

# class ZPSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ZP
#         fields = ['zp_id', 'zp_name']


# # # Vidhansabha api 

# from .models import Vidhansabha

# class VidhansabhaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vidhansabha
#         fields = ['vidhansabha_id', 'vidhansabha_name']


# # # State api

# from .models import State

# class StateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = State
#         fields = ['state_id', 'state_name']


# # cast api

# class VoterlistSerializerWithCast(serializers.ModelSerializer):
#     class Meta:
#         model = Voterlist
#         fields = ['voter_name', 'voter_cast']



# # firm login

# class FirmLoginSerializer(serializers.Serializer):
#     firm_name  = serializers.CharField()
#     firm_password = serializers.CharField()


# # firm register

# from .models import Firm

# class FirmSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Firm
#         fields = [ 'firm_name', 'firm_contact_number', 'firm_password']


# # # Religion api

# from .models import Religion
# class ReligionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Religion
#         fields = ['religion_id', 'religion_name']


# # Favour non-favour api

# from .models import Favour_non_favour
# class Favour_non_favourSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favour_non_favour
#         fields = ['favour_id', 'favour_type']



from rest_framework import serializers
from .models import Voterlist, Town, Booth

class VoterlistSerializer(serializers.ModelSerializer):
    town_name = serializers.SerializerMethodField()
    booth_name = serializers.SerializerMethodField()
    booth_id = serializers.SerializerMethodField()

    class Meta:
        model = Voterlist
        fields = ['voter_id', 'voter_name', 'voter_parent_name', 'voter_house_number', 'voter_age', 'voter_gender', 'town_name', 
                  'booth_id','booth_name', 'voter_contact_number', 'voter_cast','voter_favour_id', 'voter_constituency_id']

    def get_town_name(self, obj):
        try:
            town = Town.objects.get(town_id=obj.voter_town_id)
            return town.town_name
        except Town.DoesNotExist:
            return None

    def get_booth_name(self, obj):
        try:
            booth = Booth.objects.get(booth_id=obj.voter_booth_id)
            return booth.booth_name
        except Booth.DoesNotExist:
            return None
        
    def get_favour_type(self, validated_data):
        voter_favour_id = validated_data.get('voter_favour_id')
        if not Favour_non_favour.objects.filter(favour_id=voter_favour_id).exists():
            raise serializers.ValidationError('Invalid favour_id')
        return super().create(validated_data)
    

    def get_booth_id(self, obj):
        return obj.voter_booth_id
        


# # register api

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['user_name', 'user_phone', 'user_password']




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



# from .models import Voter
# class VoterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Voter
#         fields = '__all__'
 


class VoterlistSerializerWithCast(serializers.ModelSerializer):
    class Meta:
        model = Voterlist
        fields = ['voter_name', 'voter_cast']



# Politician login

from rest_framework import serializers

class PoliticianLoginSerializer(serializers.Serializer):
    politician_name = serializers.CharField()
    politician_password = serializers.CharField(write_only=True)


# Politician register

from .models import Politician

class PoliticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politician
        fields = [ 'politician_name', 'politician_contact_number', 'politician_password']



# # Religion api

from .models import Religion
class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ['religion_id', 'religion_name']


# Favour non-favour api

# from .models import Favour_non_favour

# class Favour_non_favourSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favour_non_favour
#         fields = ['favour_id', 'favour_type']


from .models import Favour_non_favour

class Favour_non_favourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voterlist
        fields = ['voter_id', 'voter_favour_id']


# town_user login

from .models import Town_user

class Town_userLoginSerializer(serializers.Serializer):
    town_user_name  = serializers.CharField()
    town_user_password = serializers.CharField()


# town_user register

from .models import Town_user

class Town_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town_user
        fields = [ 'town_user_name', 'town_user_contact_number', 'town_user_password', 'town_user_town_id']


# constituency wise voter api

from .models import Voterlist, Constituency

class ConstituencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituency
        fields = ['constituency_id', 'constituency_name']




