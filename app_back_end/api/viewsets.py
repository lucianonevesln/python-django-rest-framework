from rest_framework import viewsets
from app_back_end.api import serializers
from app_back_end import models

class AppBackEndViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AppBackEndSerializer
    queryset = models.DatabaseTeste.objects.all()