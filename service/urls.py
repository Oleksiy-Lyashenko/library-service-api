from django.urls import path, include
from rest_framework import routers

from service.views import BookViewSet, BorrowingViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet)
router.register("borrowings", BorrowingViewSet)

urlpatterns = [
    path("", include(router.urls), )
]

app_name = "service"
