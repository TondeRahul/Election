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



urlpatterns = [
    path('register/', UserListCreate.as_view(), name='user-list'),
    path('register/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('login/', UserLogin.as_view(), name='user-login'),  
    path('upload/', upload_file, name='upload_file'),
    path('get_voters/', get_voters, name='get_voters'),
    path('towns/', TownList.as_view(), name='town-list'),
    path('booths/', BoothList.as_view(), name='booth-list'),
    path('panchayat_samitis/', PanchayatSamitiListCreate.as_view(), name='panchayat-samiti-list-create'),
    path('panchayat_samitis/<int:pk>/', PanchayatSamitiRetrieveUpdateDestroy.as_view(), name='panchayat-samiti-detail'),
    path('zps/', ZPlistCreate.as_view(),name = 'zp-list-create'),
    path('zps/int:pk>/', ZPRetrieveUpdateDestroy.as_view(), name='zp-details'),

]


