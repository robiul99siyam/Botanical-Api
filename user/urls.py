from django.urls import path
from . import views
urlpatterns = [
    path('Register/',views.UserViewset.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activete,name='activate'),
    path("Login/",views.UserLogin.as_view(),name='login'),
    path("Logout/",views.LogOutApiview.as_view(),name='logout'),
]