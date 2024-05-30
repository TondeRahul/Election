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



urlpatterns = [
    path('register/', UserListCreate.as_view(), name='user-list'),
    path('register/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('login/', UserLogin.as_view(), name='user-login'),  
    path('upload/', upload_file, name='upload_file'),
    path('get_voters/', get_voters, name='get_voters'),

]

