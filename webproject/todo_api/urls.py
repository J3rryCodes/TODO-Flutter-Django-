from django.urls import path,include
from rest_framework.routers import DefaultRouter
from todo_api.views import TODOView

router = DefaultRouter()

router.register(r'',TODOView,basename='todo')

urlpatterns = [
    path('',include(router.urls))
]
