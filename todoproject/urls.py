from django.urls import path, include
from rest_framework import routers
from todos.views import TodoViewSet

# create the router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'todos', TodoViewSet) # register '/todos'

urlpatterns = [
    path("", include(router.urls))
]