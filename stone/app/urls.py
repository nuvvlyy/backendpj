from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stone.app import views

router = DefaultRouter()
router.register(r'stone', views.StoneViewset,base_name='stone')
router.register(r'star', views.StartypeViewSet,base_name='typestar')
router.register(r'attribute',views.AttributeModelViewSet)
router.register(r'favorite',views.FaveriteModelViewSet)
router.register(r'fb-favorite',views.FaveriteFBModelViewSet)
router.register(r'img',views.stoneIMGModelViewSet)
# router.register(r'img-sm',views.stoneIMGSMModelViewSet)

# router.register(r'attribute', views.attributeofstoneViewset)

urlpatterns = [
    # path('stone', views.StoneList.as_view()),
    # path('stone/<int:id>', views.StoneDetail.as_view())
    path('', include(router.urls))
]
