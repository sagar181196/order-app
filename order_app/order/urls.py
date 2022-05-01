from django.urls import path
from .views import OrderViewSet

urlpatterns = [
    path('',OrderViewSet.as_view({'get':'get','post':'post','delete':'delete'})),
    # path('logout',OrderViewSet.as_view({'post':'post'}))
]