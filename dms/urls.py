from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from dms.views import DocumentViewSet

router = DefaultRouter()
router.register(r'', DocumentViewSet, base_name='document')

urlpatterns = router.urls