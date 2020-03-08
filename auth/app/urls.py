from django.urls import path, include
from rest_framework.routers import DefaultRouter
from auth.app import views

router = DefaultRouter()
router.register(r'admin-user', views.UserModelViewSet)
router.register(r'user', views.UserProfileViewSet)
router.register(r'fb-user', views.FaceBookUserProfileViewSet)

# router.register(r'deauthtication', views.DeauthorizeView,base_name="deauthtication")

urlpatterns = [

    path('', include(router.urls))
]
