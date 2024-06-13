# # register, login api

# from django.urls import path
# from .views import UserListCreate, UserRetrieveUpdateDestroy
# from .views import UserLogin
# from . views import upload_file
# from .views import get_voters


# urlpatterns = [
#     path('register/', UserListCreate.as_view(), name='user-list'),
#     path('register/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
#     path('login/', UserLogin.as_view(), name='user-login'),  
#     path('upload/', upload_file, name='upload_file'),
#     path('get_voters/', get_voters, name='get_voters'),
# ]

# ###############################################################
# working code

# # register, login api

from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy
from .views import UserLogin
from . views import upload_file
from .views import get_voters
from .views import TownList
from .views import BoothList
from .views import PanchayatSamitiListCreate, PanchayatSamitiRetrieveUpdateDestroy
from .views import ZPlistCreate, ZPRetrieveUpdateDestroy
from .views import VidhansabhaListCreate, VidhansabhaRetriveUpdateDestroy
from .views import StateListCreate, StateRetriveUpdateDestroy
from .views import VoterlistListCreate, VoterlistRetrieveUpdateDestroy
from .views import get_voters_by_booth




urlpatterns = [
    path('register/', UserListCreate.as_view(), name='user-list'),
    path('register/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('login/', UserLogin.as_view(), name='user-login'),  
    path('upload/', upload_file, name='upload_file'),
    path('get_voters/', get_voters, name='get_voters'),
    path('voters/', VoterlistListCreate.as_view(), name='voter-list-create'),
    path('voters/<int:voter_id>/', VoterlistRetrieveUpdateDestroy.as_view(), name='voter-detail'),
    path('towns/', TownList.as_view(), name='town-list'),
    path('booths/', BoothList.as_view(), name='booth-list'),
    path('panchayat_samitis/', PanchayatSamitiListCreate.as_view(), name='panchayat-samiti-list-create'),
    path('panchayat_samitis/<int:pk>/', PanchayatSamitiRetrieveUpdateDestroy.as_view(), name='panchayat-samiti-detail'),
    path('zps/', ZPlistCreate.as_view(),name = 'zp-list-create'),
    path('zps/int:pk>/', ZPRetrieveUpdateDestroy.as_view(), name='zp-details'),
    path('vidhansabhas/', VidhansabhaListCreate.as_view(), name = 'vidhansabha-list-create'),
    path('vidhansabha/<int:pk>/',VidhansabhaRetriveUpdateDestroy.as_view(), name = 'vidhansabha-details'),
    path('states/', StateListCreate.as_view(), name = 'state-list-create'),
    path('states/<int:pk>/',StateRetriveUpdateDestroy.as_view(), name = 'state-details'),
    path('get_voters_by_booth/<int:booth_id>/', get_voters_by_booth, name='get_voters_by_booth'),

]


