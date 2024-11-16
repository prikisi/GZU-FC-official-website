from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views
from .views import *


urlpatterns = [
# post views
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('', views.dashboard, name='dashboard'),
path('edit/', views.edit, name='edit'),
path('', include('django.contrib.auth.urls')),  

# #Register
path('register/', views.register, name='register'),

# # change password urls
path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

# # reset password urls
path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

#Player
    # path('players/', player_list, name='player_list'),
    path('players/<int:pk>/', player_detail, name='player_detail'),
    path('players/add/', player_add, name='player_add'),
    path('players/<int:pk>/edit/', player_edit, name='player_edit'),
    path('players/<int:pk>/remove/', player_remove, name='player_remove'),
#Player_list
    path('player_list/', PlayerListView.as_view(), name='player_list'),
    path('player_dashboard/', player_dashboard, name='player_dashboard'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]