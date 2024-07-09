# # working code

# import pandas as pd
# from voterapp.models import Voterlist, Booth, Town
# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseBadRequest



# def upload_file(request):
#     if request.method == 'POST':
#         if 'files' not in request.FILES:
#             return HttpResponseBadRequest("No files uploaded")
        
#         files = request.FILES.getlist('files')
#         for file in files:
#             import_excel_data(file)
        
#         return HttpResponse("Files uploaded and data imported successfully")
    
#     return render(request, 'upload_file.html')



# import pandas as pd
# from django.db import transaction
# from voterapp.models import State, ZP, PanchayatSamiti, Town, Booth, Voterlist

# @transaction.atomic
# def import_excel_data(file):
#     df = pd.read_excel(file)
#     state_dict = {}
#     zp_dict = {}
#     panchayat_samiti_dict = {}
#     town_dict = {}
#     booth_dict = {}
#     voter_dict = {}

#     for _, row in df.iterrows():
#         state_name = row['State']
#         district_name = row['District']
#         taluka_name = row['Taluka']
#         town_name = row['Town or Village']
#         booth_name = row['Address of Polling Station']

#         # State
#         state_id = state_dict.get(state_name)
#         if state_id is None:
#             state, created = State.objects.get_or_create(state_name=state_name)
#             state_dict[state_name] = state.state_id
#             state_id = state.state_id

#         # ZP
#         zp_id = zp_dict.get(district_name)
#         if zp_id is None:
#             state_obj = State.objects.get(state_name=state_name)
#             zp, created = ZP.objects.get_or_create(zp_name=district_name, zp_state_id=state_obj.state_id)
#             zp_dict[district_name] = zp.zp_id
#             zp_id = zp.zp_id

#         # Panchayat Samiti
#         panchayat_samiti_id = panchayat_samiti_dict.get(taluka_name)
#         if panchayat_samiti_id is None:
#             zp_obj = ZP.objects.get(zp_name=district_name)
#             panchayat_samiti, created = PanchayatSamiti.objects.get_or_create(
#                 panchayat_samiti_name=taluka_name, panchayat_samiti_zp_id=zp_obj.zp_id)
#             panchayat_samiti_dict[taluka_name] = panchayat_samiti.panchayat_samiti_id
#             panchayat_samiti_id = panchayat_samiti.panchayat_samiti_id

#         # Town
#         town_id = town_dict.get(town_name)
#         if town_id is None:
#             panchayat_samiti_obj = PanchayatSamiti.objects.get(panchayat_samiti_name=taluka_name)
#             town, created = Town.objects.get_or_create(town_name=town_name, town_panchayat_samiti_id=panchayat_samiti_obj.panchayat_samiti_id)
#             town_dict[town_name] = town.town_id
#             town_id = town.town_id

#         # Booth
#         booth_id = booth_dict.get(booth_name)
#         if booth_id is None:
#             town_obj = Town.objects.get(town_name=town_name)
#             booth, created = Booth.objects.get_or_create(booth_name=booth_name, booth_town_id=town_obj.town_id)
#             booth_dict[booth_name] = booth.booth_id
#             booth_id = booth.booth_id


#         voter_id = voter_dict.get((town_name, booth_name, row['Name']))  # Adding row['Name'] for a unique identifier
#         if voter_id is None:
#             town_obj = Town.objects.get(town_name=town_name)
#             booth_obj = Booth.objects.get(booth_name=booth_name, booth_town_id=town_obj.town_id)
#             voter, created = Voterlist.objects.get_or_create(
#                 voter_name=row['Name'],
#                 voter_parent_name=row['Parent Name'],
#                 voter_house_number=row['House Number'],
#                 voter_age=row['Age'],
#                 voter_gender=row['Gender'],
#                 voter_town_id=town_obj.town_id,
#                 voter_booth_id=booth_obj.booth_id
#             )
#             voter_dict[(town_name, booth_name, row['Name'])] = voter.voter_id
#             voter_id = voter.voter_id


# # voter api

# from rest_framework import generics
# from .models import Voterlist
# from .serializers import VoterlistSerializer

# class VoterlistListCreate(generics.ListCreateAPIView):
#     queryset = Voterlist.objects.all()
#     serializer_class = VoterlistSerializer

# class VoterlistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Voterlist.objects.all()
#     serializer_class = VoterlistSerializer
#     lookup_field = 'voter_id'  # Use the primary key field as the lookup field



# # # register api

# from rest_framework import generics
# from .models import User
# from .serializers import UserSerializer

# class UserListCreate(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def perform_create(self, serializer):
#         session_id = self.request.session.get('firm_id')  # Retrieve session ID
#         serializer.save(user_firm_id=session_id) 

# class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




# # # login api

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth.hashers import check_password
# from .serializers import LoginSerializer, VoterlistSerializer
# from .models import User, Voterlist

# class UserLogin(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user_name = serializer.validated_data.get('user_name')
#             user_password = serializer.validated_data.get('user_password')

#             try:
#                 user = User.objects.get(user_name=user_name)
#             except User.DoesNotExist:
#                 return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

#             if check_password(user_password, user.user_password):
#                 voters = Voterlist.objects.filter(voter_booth_id=user.user_booth_id)
#                 serializer = VoterlistSerializer(voters, many=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # # Get users api

# from django.http import JsonResponse
# from django.db import connection

# def get_voters(request):
#     state_id_param = request.GET.get('state_id')
#     vidhansabha_id_param = request.GET.get('vidhansabha_id')
#     zp_id_param = request.GET.get('zp_id')
#     panchayat_samiti_id_param = request.GET.get('panchayat_samiti_id')
#     town_id_param = request.GET.get('town_id')
#     booth_id_param = request.GET.get('booth_id')

#     cursor = connection.cursor()
#     cursor.callproc('GetVoters', [state_id_param, vidhansabha_id_param, zp_id_param, panchayat_samiti_id_param, town_id_param, booth_id_param])
#     results = cursor.fetchall()
    
#     voters = []
#     for row in results:
#         voters.append({
#             'voter_name': row[0],
#             'town_name': row[1],
#             'booth_name': row[2]
#         })
    
#     return JsonResponse({'voters': voters})


# # # Town api

# from .models import Town
# from .serializers import TownSerializer

# class TownList(generics.ListAPIView):
#     queryset = Town.objects.all()
#     serializer_class = TownSerializer


# # # Booth api

# from .models import Booth
# from .serializers import BoothSerializer

# class BoothList(generics.ListAPIView):
#     queryset = Booth.objects.all()
#     serializer_class = BoothSerializer


# # # Panchayat_samiti api

# from .models import PanchayatSamiti
# from .serializers import PanchayatSamitiSerializer

# class PanchayatSamitiListCreate(generics.ListCreateAPIView):
#     queryset = PanchayatSamiti.objects.all()
#     serializer_class = PanchayatSamitiSerializer

# class PanchayatSamitiRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PanchayatSamiti.objects.all()
#     serializer_class = PanchayatSamitiSerializer


# # # ZP api

# from .models import ZP
# from .serializers import ZPSerializer

# class ZPlistCreate(generics.ListCreateAPIView):
#     queryset = ZP.objects.all()
#     serializer_class = ZPSerializer

# class ZPRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ZP.objects.all()
#     serializer_class = ZPSerializer


# # # vidhansabha api

# from .models import Vidhansabha
# from .serializers import VidhansabhaSerializer

# class VidhansabhaListCreate(generics.ListCreateAPIView):
#     queryset = Vidhansabha.objects.all()
#     serializer_class = VidhansabhaSerializer

# class VidhansabhaRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vidhansabha.objects.all()
#     serializer_class = VidhansabhaSerializer


# # # state api

# from .models import State
# from .serializers import StateSerializer

# class StateListCreate(generics.ListCreateAPIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer

# class StateRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = State.objects.all() 
#     serializer_class = StateSerializer


# # # get_voters_by_booth wise api

# def get_voters_by_booth(request, booth_id):
#     with connection.cursor() as cursor:
#         cursor.execute("""
#             SELECT v.voter_id, v.voter_name, b.booth_name
#             FROM tbl_voter v
#             JOIN tbl_booth b ON v.voter_booth_id = b.booth_id
#             WHERE v.voter_booth_id = %s
#         """, [booth_id])
#         results = cursor.fetchall()
    
#     voters = []
#     for row in results:
#         voters.append({
#             'voter_id': row[0],
#             'voter_name': row[1],
#             'booth_name': row[2]
#         })
    
#     return JsonResponse({'voters': voters})


# # cast api

# from .serializers import VoterlistSerializerWithCast
# from django.views import View

# class GetVoterByCastView(View):
#     def get(self, request, voter_cast):
#         voters = Voterlist.objects.filter(voter_cast=voter_cast)
#         voters_list = list(voters.values())
#         return JsonResponse(voters_list, safe=False)



# # firm login

# from .serializers import FirmLoginSerializer
# from .models import Firm 

# class FirmLogin(APIView):
#     def post(self, request):
#         serializer = FirmLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             firm_name = serializer.validated_data.get('firm_name')
#             firm_password = serializer.validated_data.get('firm_password')

#             try:
#                 firm = Firm.objects.get(firm_name=firm_name)

#             except Firm.DoesNotExist:
#                 return Response({"message": "Invalid name credentials"}, status=status.HTTP_401_UNAUTHORIZED) 


#             # if check_password(firm_password, firm.firm_password)
#             if firm_password == firm.firm_password:
#                 request.session['firm_id'] = firm.firm_id
#                 print(request.session.get('firm_id'))
#                 return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"message": "Invalid password credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# # firm register

# from .models import Firm
# from .serializers import FirmSerializer

# class FirmCreate(generics.ListCreateAPIView):
#     queryset = Firm.objects.all()
#     serializer_class = FirmSerializer


# # # Religion api

# from .models import Religion
# from .serializers import ReligionSerializer

# class ReligionListCreate(generics.ListCreateAPIView):
#     queryset = Religion.objects.all()
#     serializer_class = ReligionSerializer

# class ReligionRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Religion.objects.all() 
#     serializer_class = ReligionSerializer


# # Favour non-favour api

# from .models import Favour_non_favour
# from .serializers import Favour_non_favourSerializer

# class Favour_non_favourListCreate(generics.ListCreateAPIView):
#     queryset = Favour_non_favour.objects.all()
#     serializer_class = Favour_non_favourSerializer

# class Favour_non_favourRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Favour_non_favour.objects.all() 
#     serializer_class = Favour_non_favourSerializer




import pandas as pd
from voterapp.models import Voterlist, Booth, Town
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest



def upload_file(request):
    if request.method == 'POST':
        if 'files' not in request.FILES:
            return HttpResponseBadRequest("No files uploaded")
        
        files = request.FILES.getlist('files')
        for file in files:
            import_excel_data(file)
        
        return HttpResponse("Files uploaded and data imported successfully")
    
    return render(request, 'upload_file.html')




from django.db import transaction
@transaction.atomic
def import_excel_data(file):
    try:
        df = pd.read_excel(file)
    except Exception as e:
        # logger.error(f"Error reading Excel file: {str(e)}")
        return f"Error reading Excel file: {str(e)}"

    successful_imports = 0
    total_rows = len(df)

    data_list = df.values.tolist()

    booth_dict = {}
    town_dict = {}
    for rec in data_list:
        state_name = rec[10]
        district_name = rec[9]
        taluka_name = rec[8]
        town_name = rec[6]
        booth_name = rec[7]
        vote_name = rec[1]

        

        booth_id = None
        town_id = None
        

        state, created = State.objects.get_or_create(state_name=state_name)

        zp, created = ZP.objects.get_or_create(zp_name=district_name, zp_state_id=state.state_id)

        panchayat_samiti, created = PanchayatSamiti.objects.get_or_create(panchayat_samiti_name=taluka_name, panchayat_samiti_zp_id=zp.zp_id)
        
        if town_name not in town_dict:
            town, created = Town.objects.get_or_create(town_name=town_name, town_panchayat_samiti_id=panchayat_samiti.panchayat_samiti_id)
            town_dict[town_name] = town.town_id
            town_id = town.town_id
        else:
            town_id = town_dict[town_name]

        if booth_name not in booth_dict:
            booth, created = Booth.objects.get_or_create(booth_name=booth_name, booth_town_id=town.town_id)
            booth_dict[booth_name] = booth.booth_id
            booth_id = booth.booth_id
        else:
            booth_id = booth_dict[booth_name]
        

        #voter_name, created = Voterlist.objects.get_or_create(voter_name = vote_name, voter_town_id = town.town_id, voter_booth_id = booth.booth_id)

        vote_obj = Voterlist(
            
            voter_name = vote_name,
            voter_parent_name = rec[2],
            voter_house_number = rec[3],
            voter_age = rec[4],
            voter_gender = rec[5],
            voter_town_id = town_id,
            voter_booth_id = booth_id
        )

        vote_obj.save()



# # voter api

from rest_framework import generics
from .models import Voterlist
from .serializers import VoterlistSerializer

class VoterlistListCreate(generics.ListCreateAPIView):
    queryset = Voterlist.objects.all()
    serializer_class = VoterlistSerializer

class VoterlistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voterlist.objects.all()
    serializer_class = VoterlistSerializer
    lookup_field = 'voter_id'  



from rest_framework import generics           # code for a session login id to user
from .models import User
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        session_id = self.request.session.get('town_user_id')  # Retrieve session ID
        serializer.save(user_town_user_id=session_id) 

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# # login api

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from .serializers import LoginSerializer, VoterlistSerializer
from .models import User, Voterlist

class UserLogin(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data.get('user_name')
            user_password = serializer.validated_data.get('user_password')

            try:
                user = User.objects.get(user_name=user_name)
            except User.DoesNotExist:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

            if check_password(user_password, user.user_password):
                voters = Voterlist.objects.filter(voter_booth_id=user.user_booth_id)
                serializer = VoterlistSerializer(voters, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# # Get users api

from django.http import JsonResponse
from django.db import connection

def get_voters(request, booth_id=None):
    state_id_param = request.GET.get('state_id')
    vidhansabha_id_param = request.GET.get('vidhansabha_id')
    zp_id_param = request.GET.get('zp_id')
    panchayat_samiti_id_param = request.GET.get('panchayat_samiti_id')
    town_id_param = request.GET.get('town_id')
    booth_id_param = request.GET.get('booth_id') if booth_id is None else booth_id

    cursor = connection.cursor()
    cursor.callproc('GetVoters', [state_id_param, vidhansabha_id_param, zp_id_param, panchayat_samiti_id_param, town_id_param, booth_id_param])
    results = cursor.fetchall()
    
    voters = []
    for row in results:
        voters.append({
            'voter_id': row[0],
            'voter_name': row[1],
            'booth_name': row[2], 
            'town_name': row[3]
        })
    
    return JsonResponse({'voters': voters})



# # Town api

from .models import Town
from .serializers import TownSerializer

class TownList(generics.ListAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer


# # Booth api

from .models import Booth
from .serializers import BoothSerializer

class BoothList(generics.ListAPIView):
    queryset = Booth.objects.all()
    serializer_class = BoothSerializer
    lookup_field = 'booth_id' 


# # Panchayat_samiti API

from .models import PanchayatSamiti
from .serializers import PanchayatSamitiSerializer

class PanchayatSamitiListCreate(generics.ListCreateAPIView):
    queryset = PanchayatSamiti.objects.all()
    serializer_class = PanchayatSamitiSerializer

class PanchayatSamitiRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PanchayatSamiti.objects.all()
    serializer_class = PanchayatSamitiSerializer


# # ZP api

from .models import ZP
from .serializers import ZPSerializer

class ZPListCreate(generics.ListCreateAPIView):
    queryset = ZP.objects.all()
    serializer_class = ZPSerializer

class ZPRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZP.objects.all()
    serializer_class = ZPSerializer


# # vidhansabha api

from .models import Vidhansabha
from .serializers import VidhansabhaSerializer

class VidhansabhaListCreate(generics.ListCreateAPIView):
    queryset = Vidhansabha.objects.all()
    serializer_class = VidhansabhaSerializer

class VidhansabhaRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vidhansabha.objects.all()
    serializer_class = VidhansabhaSerializer


# # state api

from .models import State
from .serializers import StateSerializer

class StateListCreate(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer



# # get_voters_by_booth wise api

def get_voters_by_booth(request, booth_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT v.voter_id, v.voter_name, b.booth_name, voter_contact_number, voter_cast, voter_favour_id, voter_booth_id, voter_town_id
            FROM tbl_voter v
            JOIN tbl_booth b ON v.voter_booth_id = b.booth_id
            WHERE v.voter_booth_id = %s
        """, [booth_id])
        results = cursor.fetchall()
    
    voters = []
    for row in results:
        voters.append({
            'voter_id': row[0],
            'voter_name': row[1],
            'booth_name': row[2],
            'voter_contact_number' : row[3],
            'voter_cast' : row[4],
            'voter_favour_id' : row[5],
            'voter_booth_id' : row[6],
            'voter_town_id' : row[7]
        })
    
    return JsonResponse({'voters': voters})


# Get voters by cast wise

from .serializers import VoterlistSerializerWithCast
from django.views import View

class GetVoterByCastView(View):
    def get(self, request, voter_cast):
        voters = Voterlist.objects.filter(voter_cast=voter_cast)
        voters_list = list(voters.values())
        return JsonResponse(voters_list, safe=False)



# Politician login

from .serializers import PoliticianLoginSerializer
from .models import Politician

class PoliticianLoginView(APIView):
    def post(self, request):
        serializer = PoliticianLoginSerializer(data=request.data)
        if serializer.is_valid():
            username_or_contact = serializer.validated_data['politician_name']
            password = serializer.validated_data['politician_password']

            try:
                # Determine if the input is a name or contact number
                if username_or_contact.isdigit():
                    politician = Politician.objects.get(politician_contact_number=username_or_contact)
                else:
                    politician = Politician.objects.get(politician_name=username_or_contact)

                if check_password(password, politician.politician_password):
                    request.session['politician_id'] = politician.politician_id
                    return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
            except Politician.DoesNotExist:
                return Response({"error": "Politician not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# Politician register

from .models import Politician
from .serializers import PoliticianSerializer

class PoliticianCreate(generics.ListCreateAPIView):
    queryset = Politician.objects.all()
    serializer_class = PoliticianSerializer


# # Religion api

from .models import Religion
from .serializers import ReligionSerializer

class ReligionListCreate(generics.ListCreateAPIView):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer

class ReligionRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Religion.objects.all() 
    serializer_class = ReligionSerializer


# Favour non-favour api

# from .models import Favour_non_favour
# from .serializers import Favour_non_favourSerializer

# class Favour_non_favourListCreate(generics.ListCreateAPIView):
#     queryset = Favour_non_favour.objects.all()
#     serializer_class = Favour_non_favourSerializer

# class Favour_non_favourRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Favour_non_favour.objects.all() 
#     serializer_class = Favour_non_favourSerializer


from .serializers import Favour_non_favourSerializer

class Favour_non_favourRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voterlist.objects.all()
    serializer_class = Favour_non_favourSerializer



# town_user login

from .serializers import Town_userLoginSerializer
from .models import Town_user 

class Town_userLogin(APIView):
    def post(self, request):
        serializer = Town_userLoginSerializer(data=request.data)
        if serializer.is_valid():
            town_user_name = serializer.validated_data.get('town_user_name')
            town_user_password = serializer.validated_data.get('town_user_password')

            try:
                town_user = Town_user.objects.get(town_user_name=town_user_name)

            except Town_user.DoesNotExist:
                return Response({"message": "Invalid name credentials"}, status=status.HTTP_401_UNAUTHORIZED) 


            # if check_password(town_user_password, town_user.town_user_password)
            if town_user_password == town_user.town_user_password:
                request.session['town_user_id'] = town_user.town_user_id
                print(request.session.get('town_user_id'))
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid password credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# town_user register

from .models import Town_user
from .serializers import Town_userSerializer

class Town_userCreate(generics.ListCreateAPIView):
    queryset = Town_user.objects.all()
    serializer_class = Town_userSerializer

    def perform_create(self, serializer):
        session_id = self.request.session.get('politician_id')
        serializer.save(town_user_politician_id=session_id) 


# get_town_voter

def get_town_voter_list(request, town_user_town_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                v.voter_id, 
                v.voter_name, 
                b.booth_id, 
                b.booth_name, 
                t.town_id, 
                t.town_name,
                v.voter_parent_name,
                v.voter_house_number,
                v.voter_age,
                v.voter_gender,
                v.voter_contact_number
            FROM 
                tbl_voter v
            JOIN 
                tbl_booth b ON v.voter_booth_id = b.booth_id
            JOIN 
                tbl_town t ON b.booth_town_id = t.town_id
            JOIN 
                tbl_town_user tu ON t.town_id = tu.town_user_town_id
            WHERE 
                tu.town_user_town_id = %s;
        """, [town_user_town_id])
        results = cursor.fetchall()

    voters = []
    for row in results:
        voters.append({
            'voter_id': row[0],
            'voter_name': row[1],
            'booth_id': row[2],
            'booth_name': row[3],
            'town_id': row[4],
            'town_name': row[5],
            'voter_parent_name': row[6],
            'voter_house_number': row[7],
            'voter_age': row[8],
            'voter_gender': row[9],
            #'voter_cast': row[10],
            'voter_contact_number': row[10]
        })

    return JsonResponse({'voters': voters})


# get_taluka_voter_list

def get_taluka_voter_list(request, politician_taluka_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                v.voter_id, 
                v.voter_name, 
                b.booth_id, 
                b.booth_name, 
                t.town_id, 
                t.town_name,
                v.voter_parent_name,
                v.voter_house_number,
                v.voter_age,
                v.voter_gender,
                v.voter_contact_number
            FROM 
                tbl_voter v
            JOIN 
                tbl_booth b ON v.voter_booth_id = b.booth_id
            JOIN 
                tbl_town t ON b.booth_town_id = t.town_id
            JOIN 
                tbl_panchayat_samiti ps ON ps.panchayat_samiti_id = t.town_panchayat_samiti_id
            JOIN 
                tbl_politician p ON p.politician_taluka_id = ps.panchayat_samiti_id
            
            
            WHERE 
                p.politician_taluka_id = %s;
        """, [politician_taluka_id])
        results = cursor.fetchall()

    voters = []
    for row in results:
        voters.append({
            'voter_id': row[0],
            'voter_name': row[1],
            'booth_id': row[2],
            'booth_name': row[3],
            'town_id': row[4],
            'town_name': row[5],
            'voter_parent_name': row[6],
            'voter_house_number': row[7],
            'voter_age': row[8],
            'voter_gender': row[9],
            #'voter_cast': row[10],
            'voter_contact_number': row[10]
        })

    return JsonResponse({'voters': voters})


# constituency wise voter api

from .serializers import VoterlistSerializer

class VotersByConstituencyView(generics.ListAPIView):
    serializer_class = VoterlistSerializer

    def get_queryset(self):
        constituency_id = self.kwargs['constituency_id']
        return Voterlist.objects.filter(voter_constituency_id=constituency_id)


