from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('api/user/', views.UserListCreate.as_view() ),
    path('api/profile/', views.ProfileList.as_view() ),
    path('api/profile/<int:pk>/', views.ProfileDetail.as_view() ),
]
