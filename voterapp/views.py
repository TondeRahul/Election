# # # register api

# from rest_framework import generics
# from .models import User
# from .serializers import UserSerializer

# class UserListCreate(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




# # # login api

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth.hashers import check_password
# from .serializers import LoginSerializer
# from .models import User

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
#                 return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ##########################################################
# working code


import pandas as pd
from voterapp.models import Voterlist, Booth, Town
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# def upload_file(request):
#     return HttpResponse("Upload File View")

# def upload_file(request):
#     if request.method == 'POST':
#         if 'file' not in request.FILES:
#             return HttpResponseBadRequest("No file uploaded")
#         file = request.FILES['file']
#         import_excel_data(file)
#         return HttpResponse("File uploaded and data imported successfully")
#     return render(request, 'upload_file.html')

# def import_excel_data(file_path):
#     df = pd.read_excel(file_path)
#     for _, row in df.iterrows():
#         town_name = row['Town or Village']
#         booth_name = row['Address of Polling Station']
        
#         town, created = Town.objects.get_or_create(town_name=town_name, defaults={'town_panchayat_samiti_id': 0})
        
#         booth, created = Booth.objects.get_or_create(booth_name=booth_name, defaults={'booth_town_id': town.town_id})  
        
#         voter = Voterlist(
#             voter_name=row['Name'],
#             voter_parent_name=row['Parent Name'],
#             voter_house_number=row['House Number'],
#             voter_age=row['Age'],
#             voter_gender=row['Gender'],
#             voter_town_id=town.town_id,  
#             voter_booth_id=booth.booth_id  
#         )
#         voter.save()



def upload_file(request):
    if request.method == 'POST':
        if 'files' not in request.FILES:
            return HttpResponseBadRequest("No files uploaded")
        
        files = request.FILES.getlist('files')
        for file in files:
            import_excel_data(file)
        
        return HttpResponse("Files uploaded and data imported successfully")
    
    return render(request, 'upload_file.html')


# import pandas as pd
# from django.db import transaction
# from .models import State, ZP, PanchayatSamiti, Town, Booth, Voterlist

# @transaction.atomic
# def import_excel_data(file):
#     df = pd.read_excel(file)
#     for _, row in df.iterrows():
#         state_name = row['State']
#         district_name = row['District']
#         taluka_name = row['Taluka']
#         town_name = row['Town or Village']
#         booth_name = row['Address of Polling Station']
        
#         state, _ = State.objects.get_or_create(state_name=state_name)
        
#         zp, _ = ZP.objects.get_or_create(zp_name=district_name, defaults={'zp_state_id': state.state_id})
        
#         panchayat_samiti, _ = PanchayatSamiti.objects.get_or_create(panchayat_samiti_name=taluka_name, defaults={'panchayat_samiti_zp_id': zp.zp_id})
        
#         town, _ = Town.objects.get_or_create(town_name=town_name, defaults={'town_panchayat_samiti_id': panchayat_samiti.panchayat_samiti_id})
        
#         booth, _ = Booth.objects.get_or_create(booth_name=booth_name, defaults={'booth_town_id': town.town_id})
        
#         # Creating Voterlist object and saving it
#         voter = Voterlist.objects.create(
#             voter_name=row['Name'],
#             voter_parent_name=row['Parent Name'],
#             voter_house_number=row['House Number'],
#             voter_age=row['Age'],
#             voter_gender=row['Gender'],
#             voter_town_id=town.town_id,
#             voter_booth_id=booth.booth_id
#         )


import pandas as pd
from django.db import transaction
from voterapp.models import State, ZP, PanchayatSamiti, Town, Booth, Voterlist

@transaction.atomic
def import_excel_data(file):
    df = pd.read_excel(file)
    state_dict = {}
    zp_dict = {}
    panchayat_samiti_dict = {}
    town_dict = {}
    booth_dict = {}
    voter_dict = {}

    for _, row in df.iterrows():
        state_name = row['State']
        district_name = row['District']
        taluka_name = row['Taluka']
        town_name = row['Town or Village']
        booth_name = row['Address of Polling Station']

        # State
        state_id = state_dict.get(state_name)
        if state_id is None:
            state, created = State.objects.get_or_create(state_name=state_name)
            state_dict[state_name] = state.state_id
            state_id = state.state_id

        # ZP
        zp_id = zp_dict.get(district_name)
        if zp_id is None:
            state_obj = State.objects.get(state_name=state_name)
            zp, created = ZP.objects.get_or_create(zp_name=district_name, zp_state_id=state_obj.state_id)
            zp_dict[district_name] = zp.zp_id
            zp_id = zp.zp_id

        # Panchayat Samiti
        panchayat_samiti_id = panchayat_samiti_dict.get(taluka_name)
        if panchayat_samiti_id is None:
            zp_obj = ZP.objects.get(zp_name=district_name)
            panchayat_samiti, created = PanchayatSamiti.objects.get_or_create(
                panchayat_samiti_name=taluka_name, panchayat_samiti_zp_id=zp_obj.zp_id)
            panchayat_samiti_dict[taluka_name] = panchayat_samiti.panchayat_samiti_id
            panchayat_samiti_id = panchayat_samiti.panchayat_samiti_id

        # Town
        town_id = town_dict.get(town_name)
        if town_id is None:
            panchayat_samiti_obj = PanchayatSamiti.objects.get(panchayat_samiti_name=taluka_name)
            town, created = Town.objects.get_or_create(town_name=town_name, town_panchayat_samiti_id=panchayat_samiti_obj.panchayat_samiti_id)
            town_dict[town_name] = town.town_id
            town_id = town.town_id

        # Booth
        booth_id = booth_dict.get(booth_name)
        if booth_id is None:
            town_obj = Town.objects.get(town_name=town_name)
            booth, created = Booth.objects.get_or_create(booth_name=booth_name, booth_town_id=town_obj.town_id)
            booth_dict[booth_name] = booth.booth_id
            booth_id = booth.booth_id


        voter_id = voter_dict.get((town_name, booth_name, row['Name']))  # Adding row['Name'] for a unique identifier
        if voter_id is None:
            town_obj = Town.objects.get(town_name=town_name)
            booth_obj = Booth.objects.get(booth_name=booth_name, booth_town_id=town_obj.town_id)
            voter, created = Voterlist.objects.get_or_create(
                voter_name=row['Name'],
                voter_parent_name=row['Parent Name'],
                voter_house_number=row['House Number'],
                voter_age=row['Age'],
                voter_gender=row['Gender'],
                voter_town_id=town_obj.town_id,
                voter_booth_id=booth_obj.booth_id
            )
            voter_dict[(town_name, booth_name, row['Name'])] = voter.voter_id
            voter_id = voter.voter_id



# voter api

from rest_framework import generics
from .models import Voterlist
from .serializers import VoterlistSerializer

class VoterlistListCreate(generics.ListCreateAPIView):
    queryset = Voterlist.objects.all()
    serializer_class = VoterlistSerializer

class VoterlistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voterlist.objects.all()
    serializer_class = VoterlistSerializer
    lookup_field = 'voter_id'  # Use the primary key field as the lookup field



# # register api

from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




# # login api

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.contrib.auth.hashers import check_password
from .serializers import LoginSerializer
from .models import User

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
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # Get users api

from django.http import JsonResponse
from django.db import connection

def get_voters(request):
    state_id_param = request.GET.get('state_id')
    vidhansabha_id_param = request.GET.get('vidhansabha_id')
    zp_id_param = request.GET.get('zp_id')
    panchayat_samiti_id_param = request.GET.get('panchayat_samiti_id')
    town_id_param = request.GET.get('town_id')
    booth_id_param = request.GET.get('booth_id')

    cursor = connection.cursor()
    cursor.callproc('GetVoters', [state_id_param, vidhansabha_id_param, zp_id_param, panchayat_samiti_id_param, town_id_param, booth_id_param])
    results = cursor.fetchall()
    
    voters = []
    for row in results:
        voters.append({
            'voter_name': row[0],
            'town_name': row[1],
            'booth_name': row[2]
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


# # Panchayat_samiti api

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

class ZPlistCreate(generics.ListCreateAPIView):
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
            SELECT v.voter_id, v.voter_name, b.booth_name
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
            'booth_name': row[2]
        })
    
    return JsonResponse({'voters': voters})

