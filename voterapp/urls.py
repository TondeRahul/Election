# # working code

# from django.urls import path
# from .views import UserListCreate, UserRetrieveUpdateDestroy
# from .views import UserLogin
# from . views import upload_file
# from .views import get_voters
# from .views import TownList
# from .views import BoothList
# from .views import PanchayatSamitiListCreate, PanchayatSamitiRetrieveUpdateDestroy
# from .views import ZPlistCreate, ZPRetrieveUpdateDestroy
# from .views import VidhansabhaListCreate, VidhansabhaRetriveUpdateDestroy
# from .views import StateListCreate, StateRetriveUpdateDestroy
# from .views import VoterlistListCreate, VoterlistRetrieveUpdateDestroy
# from .views import get_voters_by_booth
# from .views import GetVoterByCastView
# from .views import FirmLogin
# from .views import FirmCreate
# from .views import ReligionListCreate
# from .views import ReligionRetriveUpdateDestroy
# from .views import Favour_non_favourListCreate
# from .views import Favour_non_favourRetriveUpdateDestroy



# urlpatterns = [
#     path('register/', UserListCreate.as_view(), name='user-list'),
#     path('register/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
#     path('login/', UserLogin.as_view(), name='user-login'),  
#     path('upload/', upload_file, name='upload_file'),
#     path('get_voters/', get_voters, name='get_voters'),
#     path('voters/', VoterlistListCreate.as_view(), name='voter-list-create'),
#     path('voters/<int:voter_id>/', VoterlistRetrieveUpdateDestroy.as_view(), name='voter-detail'),
#     path('towns/', TownList.as_view(), name='town-list'),
#     path('booths/', BoothList.as_view(), name='booth-list'),
#     path('panchayat_samitis/', PanchayatSamitiListCreate.as_view(), name='panchayat-samiti-list-create'),
#     path('panchayat_samitis/<int:pk>/', PanchayatSamitiRetrieveUpdateDestroy.as_view(), name='panchayat-samiti-detail'),
#     path('zps/', ZPlistCreate.as_view(),name = 'zp-list-create'),
#     path('zps/<int:pk>/', ZPRetrieveUpdateDestroy.as_view(), name='zp-details'),
#     path('vidhansabhas/', VidhansabhaListCreate.as_view(), name = 'vidhansabha-list-create'),
#     path('vidhansabha/<int:pk>/',VidhansabhaRetriveUpdateDestroy.as_view(), name = 'vidhansabha-details'),
#     path('states/', StateListCreate.as_view(), name = 'state-list-create'),
#     path('states/<int:pk>/',StateRetriveUpdateDestroy.as_view(), name = 'state-details'),
#     path('get_voters_by_booth/<int:booth_id>/', get_voters_by_booth, name='get_voters_by_booth'),
#     path('voters_by_cast/<str:voter_cast>/', GetVoterByCastView.as_view(), name='voter-by-cast'),
#     path('firm_login/', FirmLogin.as_view(), name='firm-login'),
#     path('firm_register/', FirmCreate.as_view(), name='user-list'),
#     path('religion/', ReligionListCreate.as_view(), name='religion-list'),
#     path('religion/<int:pk>/', ReligionRetriveUpdateDestroy.as_view(), name='religion-detail'),
#     path('favour/', Favour_non_favourListCreate.as_view(), name='Favour_non_favour-list'),
#     path('favour/<int:pk>/', Favour_non_favourRetriveUpdateDestroy.as_view(), name='Favour_non_favour-detail'),


# ]


from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy
from .views import UserLogin
from .views import upload_file
from .views import get_voters
from .views import TownList
from .views import BoothList
from .views import PanchayatSamitiListCreate, PanchayatSamitiRetrieveUpdateDestroy
from .views import ZPListCreate, ZPRetrieveUpdateDestroy
from .views import VidhansabhaListCreate, VidhansabhaRetriveUpdateDestroy
from .views import StateListCreate, StateRetriveUpdateDestroy
from .views import VoterlistListCreate, VoterlistRetrieveUpdateDestroy
from .views import get_voters_by_booth
from .views import GetVoterByCastView
from .views import PoliticianLoginView
from .views import PoliticianCreate
from .views import ReligionListCreate
from .views import ReligionRetriveUpdateDestroy
# from .views import Favour_non_favourListCreate
from .views import Favour_non_favourRetriveUpdateDestroy
from .views import Town_userLogin
from .views import Town_userCreate
from .views import get_town_voter_list
from .views import get_taluka_voter_list
from .views import VotersByConstituencyView




urlpatterns = [
    path('register/', UserListCreate.as_view(), name='user-list'),
    path('register/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('login/', UserLogin.as_view(), name='user-login'), 
    path('upload/', upload_file, name='upload_file'),
    path('get_voters/', get_voters, name='get_voters'),
    path('get_voters/<int:booth_id>/', get_voters, name='get_voters'),                          # getting error for fetch perticular voter 
    path('towns/', TownList.as_view(), name='town-list'),
    path('booths/', BoothList.as_view(), name='booth-list'),
    path('booths/<int:booth_id>/', BoothList.as_view(), name='booth-detail'),
    path('panchayat_samitis/', PanchayatSamitiListCreate.as_view(), name='panchayat-samiti-list-create'),
    path('panchayat_samitis/<int:pk>/', PanchayatSamitiRetrieveUpdateDestroy.as_view(), name='panchayat-samiti-detail'),
    path('zps/', ZPListCreate.as_view(),name = 'zp-list-create'),
    path('zps/<int:pk>/', ZPRetrieveUpdateDestroy.as_view(), name='zp-details'),
    path('vidhansabhas/', VidhansabhaListCreate.as_view(), name = 'vidhansabha-list-create'),
    path('vidhansabha/<int:pk>/',VidhansabhaRetriveUpdateDestroy.as_view(), name = 'vidhansabha-details'),
    path('states/', StateListCreate.as_view(), name = 'state-list-create'),
    path('states/<int:pk>/',StateRetriveUpdateDestroy.as_view(), name = 'state-details'),
    path('voters/', VoterlistListCreate.as_view(), name='voter-list-create'),
    path('voters/<int:voter_id>/', VoterlistRetrieveUpdateDestroy.as_view(), name='voter-detail'),
    path('get_voters_by_booth/<int:booth_id>/', get_voters_by_booth, name='get_voters_by_booth'),
    path('get_voters_by_booth/<int:booth_id>/<int:voter_id>/', get_voters, name='voter_detail'),
    path('voters_by_cast/<str:voter_cast>/', GetVoterByCastView.as_view(), name='voter-by-cast'),
    path('politician_login/', PoliticianLoginView.as_view(), name='politician-login'),
    path('politician_register/', PoliticianCreate.as_view(), name='Politician-list'), 
    path('religion/', ReligionListCreate.as_view(), name='religion-list'),
    path('religion/<int:pk>/', ReligionRetriveUpdateDestroy.as_view(), name='religion-detail'),
    # path('favour/', Favour_non_favourListCreate.as_view(), name='Favour_non_favour-list'),
    path('favour/<int:pk>/', Favour_non_favourRetriveUpdateDestroy.as_view(), name='Favour_non_favour-detail'),
    path('town_user_login/', Town_userLogin.as_view(), name='town_user-login'),
    path('town_user_register/', Town_userCreate.as_view(), name='town_user-list'), 
    path('get_town_voter_list/<int:town_user_town_id>/', get_town_voter_list, name='get_voters_by_town_user'),
    path('get_taluka_voter_list/<int:politician_taluka_id>/', get_taluka_voter_list, name='get_voters_by_town_user'),
    path('constituency/<int:constituency_id>/', VotersByConstituencyView.as_view(), name='voters-by-constituency'),


]
