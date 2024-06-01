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
from voterapp.models import Voter, Booth, Town
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# def upload_file(request):
#     return HttpResponse("Upload File View")

def upload_file(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return HttpResponseBadRequest("No file uploaded")
        file = request.FILES['file']
        import_excel_data(file)
        return HttpResponse("File uploaded and data imported successfully")
    return render(request, 'upload_file.html')

def import_excel_data(file_path):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        town_name = row['Town or Village']
        booth_name = row['Address of Polling Station']
        
        town, created = Town.objects.get_or_create(town_name=town_name, defaults={'town_panchayat_samiti_id': 0})
        
        booth, created = Booth.objects.get_or_create(booth_name=booth_name, defaults={'booth_town_id': town.town_id})  
        
        voter = Voter(
            voter_name=row['Name'],
            voter_parent_name=row['Parent Name'],
            voter_house_number=row['House Number'],
            voter_age=row['Age'],
            voter_gender=row['Gender'],
            voter_town_id=town.town_id,  
            voter_booth_id=booth.booth_id  
        )
        voter.save()

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

