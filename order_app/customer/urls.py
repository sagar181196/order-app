from django.urls import path
from .views import UserViewSet,Login,Logout,StripeViewSet


urlpatterns = [
    path('',UserViewSet.as_view({'get':'list','post':'post'})),
    path('login',Login.as_view({'get':'list','post':'post'})),
    path('logout',Logout.as_view({'get':'list','post':'post'})),
    path('stripe',StripeViewSet.as_view({'post':'post'})),
]