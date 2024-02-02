from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, userLogadoViewset, userLogadoProfileViewset
from rest_framework.authtoken import views
from product.views import productViewSet, messageViewSet, bagViewSet, sacoleiraProducts, productDetail, productNoteViewSet
from account.views import profileViewset, sacoleirasViewset, profileDetail, haveProfile, reviewsViewSet, rankingProfileViewSet, reviewsProfileMedia, lojistaViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'messages', messageViewSet)
router.register(r'userLogado', userLogadoViewset, basename='userlogado')
router.register(r'userLogadoProfile', userLogadoProfileViewset, basename='userlogadoprofile')
router.register(r'bag', bagViewSet, basename='bag')
router.register(r'products', productViewSet)
router.register(r'productNote', productNoteViewSet)
router.register(r'profile', profileViewset, basename='profile')
router.register(r'sacoleiras', sacoleirasViewset, basename='sacoleiras')
router.register(r'profileverify', haveProfile, basename='profileverify')
router.register(r'reviews', reviewsViewSet, basename='reviews')
router.register(r'ranking', rankingProfileViewSet, basename='ranking')
router.register(r'lojista', lojistaViewSet, basename='lojista')


urlpatterns = [
    path('', include(router.urls)),
    path('sacoleiras/<int:id>/products/', sacoleiraProducts.as_view()),
    path('sacoleiras/<int:id>/products/<int:pk>', productDetail.as_view()),
    path('reviewsmedia/<int:pk>/', reviewsProfileMedia.as_view()),
    path('profileDetail/<int:pk>/', profileDetail.as_view()),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
