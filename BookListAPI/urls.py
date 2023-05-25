from django.urls import path
from rest_framework import routers
from .views import books, Orders, BookView

router = routers.DefaultRouter(trailing_slash=False)
router.register("books", BookView, basename='books')
urlpatterns = router.urls
