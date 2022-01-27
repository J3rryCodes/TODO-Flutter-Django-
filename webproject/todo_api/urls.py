from django.urls import path,include
from rest_framework.routers import SimpleRouter
from todo_api.views import TODOView

router = SimpleRouter()

router.register('todo',TODOView,basename='todo')

urlpatterns = router.urls
