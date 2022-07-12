from rest_framework.routers import SimpleRouter

# Views
from api.views.breads_view import BreadsViewset
from api.views.meats_view import MeatsViewset
from api.views.orders_view import OrdersViewset


# Routers
router = SimpleRouter()

router.register('breads', BreadsViewset)
router.register('meats', MeatsViewset)
router.register('orders', OrdersViewset)
