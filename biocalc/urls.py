from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import routers
from rest_framework.authentication import SessionAuthentication
from .view_sets import (
    FishCategoryViewSet,
    FishViewSet,
    PlantCategoryViewSet,
    PlantViewSet,
    TankViewSet,
    UsersViewSet,
    UserProfilesViewSet,
    SocialSegmentViewSet,
    CommentViewSet,
    ItemGalleryImageViewSet,
    ItemSellingDataViewSet,
    OrderViewSet,
    OrderItemViewSet,
    PaymentViewSet,
    StripeCheckoutSessionCreateAPIView,
    StripeWebhookAPIView,
    CheckoutAPIView,
    AddressViewSet,
    )

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "biocalc"

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'users-profiles', UserProfilesViewSet)

router.register(r'fishes', FishViewSet)
router.register(r'plants', PlantViewSet)
router.register(r'tanks', TankViewSet)

router.register(r'fish-category', FishCategoryViewSet)
router.register(r'plants-category', PlantCategoryViewSet)

router.register(r'social', SocialSegmentViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'gallery', ItemGalleryImageViewSet)
router.register(r'sell-data', ItemSellingDataViewSet)

router.register(r'^(?P<order_id>\d+)/order-items', OrderItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('protected', views.protected, name='protected'),
    path('pro-admin', views.protected_set, name='protected'),
    path('send-order', views.order_handler, name='send-order'),

    path('api/', include(router.urls)),

    path('api/user/', views.ProfileView.as_view(), name='current_user'),

    path('api/login/', views.APILoginView.as_view(), name='login_token'),
    path('api/logout/', views.APILogoutView.as_view(), name='logout_token'),
    path('api/registration/', views.APIRegistrationView.as_view(), name='auth_registration'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    
    path('stripe/create-checkout-session/<int:order_id>/',
         StripeCheckoutSessionCreateAPIView.as_view(), name='checkout_session'),
    path('stripe/webhook/', StripeWebhookAPIView.as_view(), name='stripe_webhook'),
    path('checkout/<int:pk>/', CheckoutAPIView.as_view(), name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)