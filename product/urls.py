from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include

router = DefaultRouter()
router.register("list",views.ProductViewset)
router.register("productTag",views.ProductTagViewset)
router.register("reviewer",views.reviewViewset)

urlpatterns = [
    path("",include(router.urls)),
]