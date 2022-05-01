from django.urls import path
from .views import ProductViewSet,ProductDetailViewSet

urlpatterns = [
    path('',ProductViewSet.as_view({'get':'get','post':'post'})),
    path('<int:product_id>',ProductDetailViewSet.as_view({'put':'put','delete':'delete'})),
]