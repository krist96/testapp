from rest_framework.routers import SimpleRouter

from ..todos.views import TodoViewSet

router = SimpleRouter()

router.register("", TodoViewSet, basename="todos")

urlpatterns = router.urls