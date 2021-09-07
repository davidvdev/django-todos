from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    # give it the main query for the index route
    queryset = Todo.objects.all()
    # pass the serializer for serializing
    serializer_class = TodoSerializer
    # optional premissions
    permission_classes = [permissions.AllowAny]