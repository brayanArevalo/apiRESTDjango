from .models import asignatura, asignaturaxgrupo, estudiante, grupo, maestra, profesor
from rest_framework import viewsets, permissions
from .serializers import asignaturaSerializer, asignaturaxgrupoSerializer, grupoSerializer,estudianteSerializer, maestraSerializer, profesorSerializer

class grupoViewSet(viewsets.ModelViewSet):
    queryset = grupo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = grupoSerializer

class estudianteViewSet(viewsets.ModelViewSet):
    queryset = estudiante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = estudianteSerializer

class profesorViewSet(viewsets.ModelViewSet):
    queryset = profesor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = profesorSerializer

class maestraViewSet(viewsets.ModelViewSet):
    queryset = maestra.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = maestraSerializer

class asignaturaViewSet(viewsets.ModelViewSet):
    queryset = asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = asignaturaSerializer

class asignaturaxgrupoViewSet(viewsets.ModelViewSet):
    queryset = asignaturaxgrupo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = asignaturaxgrupoSerializer