from django.urls import path
from .views import get_users, create_user, user_detail, get_pet_statuses, create_pet_statuses, pet_statuses_detail

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail'),

    path('pet_statuses/', get_pet_statuses, name='get_pet_statuses'),
    path('pet_statuses/create/', create_pet_statuses, name='create_pet_statuses'),
    path('pet_statuses/<int:pk>', pet_statuses_detail, name='pet_statuses_detail')
]