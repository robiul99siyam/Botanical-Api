from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("benner/",include("benner.urls")),
    path("achive/",include("achive_logo.urls")),
    path("dailyProduct/",include("Daily_product.urls")),
    path("feature/",include("feature_product.urls")),
    path("product/",include("product.urls")),
    path("order/",include("order.urls")),
    path("user/",include("user.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)