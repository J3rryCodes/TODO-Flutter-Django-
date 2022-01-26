from django.urls import path
from profile_api.views import LoginView, RegistratrionView, LogoutView


urlpatterns = [
     path('login/',LoginView.as_view()),
     path('registration/',RegistratrionView.as_view()),
     path('logout/',LogoutView.as_view())
]
