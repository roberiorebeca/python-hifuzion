from rest_framework import routers

from hifuzion.contabilidade.views import ClienteViewSet, PlanoContaViewSet, TodoViewSet

router = routers.DefaultRouter()

router.register('clientes', ClienteViewSet)
router.register('contas', PlanoContaViewSet)
router.register('todos', TodoViewSet)

urlpatterns = router.urls
