from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BorrowerViewSet, BorrowingViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowers', BorrowerViewSet)
router.register(r'borrowings', BorrowingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
