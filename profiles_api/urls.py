from django.urls import path, include #include used to get and include rest URLs
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #no need for / since Router will add
router.register('profile', views.UserProfileViewSet) #no need to provide base_name, since we have a queryset inside UserProfileViewSet
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls)), #urls used are generated automatically
]
