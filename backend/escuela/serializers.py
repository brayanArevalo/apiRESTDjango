from rest_framework import serializers
from .models import asignatura, asignaturaxgrupo, estudiante, grupo, maestra, profesor

class grupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = grupo
        fields = '__all__'

class estudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = estudiante
        fields = '__all__'

class profesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = profesor
        fields = '__all__'

class maestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = maestra
        fields = '__all__'

class asignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = asignatura
        fields = '__all__'

class asignaturaxgrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = asignaturaxgrupo
        fields = '__all__'