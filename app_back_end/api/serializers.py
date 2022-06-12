from rest_framework import serializers
from app_back_end import models

class AppBackEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DatabaseTeste
        fields = '__all__'