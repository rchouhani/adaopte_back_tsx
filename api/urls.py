from django.urls import path
from .views import get_users, create_user, user_detail, get_pet_statuses, create_pet_statuses, pet_statuses_detail, get_admins, create_admins, admins_detail, get_availabilities, create_availabilities, availabilities_detail, get_donations, create_donations, donations_detail, get_pets, create_pets, pets_detail, get_petting_dates, create_petting_dates, petting_dates_detail, get_adoptions, create_adoptions, adoptions_detail
from .views import ProtectedView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="api-register"),

    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail'),

    path('pet_statuses/', get_pet_statuses, name='get_pet_statuses'),
    path('pet_statuses/create/', create_pet_statuses, name='create_pet_statuses'),
    path('pet_statuses/<int:pk>', pet_statuses_detail, name='pet_statuses_detail'),

    path('admins/', get_admins, name='get_admins'),
    path('admins/create/', create_admins, name='create_admins'),
    path('admins/<int:pk>', admins_detail, name='admins_detail'),

    path('availabilities/', get_availabilities, name='get_availabilities'),
    path('availabilities/create/', create_availabilities, name='create_availabilities'),
    path('availabilities/<int:pk>', availabilities_detail, name='availabilities_detail'),

    path('donations/', get_donations, name='get_donations'),
    path('donations/create/', create_donations, name='create_donations'),
    path('donations/<int:pk>', donations_detail, name='donations_detail'),
    
    path('pets/', get_pets, name='get_pets'),
    path('pets/create/', create_pets, name='create_pets'),
    path('pets/<int:pk>', pets_detail, name='pets_detail'),
        
    path('petting_dates/', get_petting_dates, name='get_petting_dates'),
    path('petting_dates/create/', create_petting_dates, name='create_petting_dates'),
    path('petting_dates/<int:pk>', petting_dates_detail, name='petting_dates_detail'),
            
    path('adoptions/', get_adoptions, name='get_adoptions'),
    path('adoptions/create/', create_adoptions, name='create_adoptions'),
    path('adoptions/<int:pk>', adoptions_detail, name='adoptions_detail')
]