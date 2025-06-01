from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/my-profile', views.profile_page, name='profile'),
    path('profile/my-notes', views.profile_notes_page, name='notes'),
    path('<str:username>/follow/', views.follow_user, name='follow'),
    path('<str:username>/unfollow/', views.unfollow_user, name='unfollow'),
    path('toggle/<str:username>/', views.toggle_follow_user, name='toggle_follow_user'),
    path('togglermv/<str:username>/', views.rmv_follower, name='rmv_follower'),
    path('<str:username>/', views.other_user_profile, name='other_profile'),
    path('<str:username>/followers/', views.FollowersView.as_view(), name='followers'),
    path('<str:username>/following/', views.FollowingView.as_view(), name='following'),
]