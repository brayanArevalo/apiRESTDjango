from rest_framework import routers
from .api import asignaturaViewSet, asignaturaxgrupoViewSet, estudianteViewSet, grupoViewSet, maestraViewSet, profesorViewSet

router = routers.DefaultRouter()

router.register('api/grupos',grupoViewSet,'grupos')
router.register('api/estudiantes',estudianteViewSet,'estudiantes')
router.register('api/profesores',profesorViewSet,'profesores')
router.register('api/asignaturas',asignaturaViewSet,'asignaturas')
router.register('api/asignaturasxgrupo',asignaturaxgrupoViewSet,'asignaturasxgrupo')
router.register('api/maestra',maestraViewSet,'maestra')


urlpatterns = router.urls