from django.urls import path, include

from .views import AmbassadorAPIView, ProductGenericAPIView, LinkAPIView, OrderAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('ambassadors', AmbassadorAPIView.as_view()),
    path('products', ProductGenericAPIView.as_view()),
    path('products/<str:pk>', ProductGenericAPIView.as_view()),
    path('users/<str:pk>/links', LinkAPIView.as_view()),
    path('orders', OrderAPIView.as_view()),
]
