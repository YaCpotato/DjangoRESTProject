from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('tsunlist', views.TsunListViewSet)
#router.register('tsunlist_getall',views.TsunListViewSet.getAllTsunList())

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]
