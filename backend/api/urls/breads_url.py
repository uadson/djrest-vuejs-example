from rest_framework.routers import SimpleRouter

from api.views.breads_view import BreadsViewset


router = SimpleRouter()
router.register('breads', BreadsViewset)
