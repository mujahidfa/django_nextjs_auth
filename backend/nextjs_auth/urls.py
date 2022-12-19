from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from nextjs_auth import views
from nextjs_auth.views import ExampleTokenObtainPairView

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/token/", ExampleTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
