from django.urls import path
from .views import (
    DesignerRegisterView,
    DesignerLoginView,
    DesignerListView,
    BuyerRequestCreateView,
)

urlpatterns = [
    path('designers/register/', DesignerRegisterView.as_view(), name='designer-register'),
    path('designers/login/', DesignerLoginView.as_view(), name='designer-login'),
    path('designers/', DesignerListView.as_view(), name='designer-list'),
    path('requests/', BuyerRequestCreateView.as_view(), name='buyer-request'),
]
