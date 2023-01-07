from rest_framework import routers
from .api import ProjectsViewSet

router = routers.DefaultRouter()

router.register('api/project', ProjectsViewSet, 'project')
urlpatterns = router.urls