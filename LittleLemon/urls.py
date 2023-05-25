from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items', views.MenuItemsViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>', views.category_detail, name='category-detail'),
    path('secret', views.secret),
    path('login', obtain_auth_token),
    path("is_manager", views.manager),
    path('throttle', views.throttle)
]
