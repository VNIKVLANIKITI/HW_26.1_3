from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter
from education.views import LessonViewSet, CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetriveAPIView, LessonUpdateAPIView, LessonDestroyAPIView
from education.views import CourceProductCreate, CourcePriceCreate, CourceCheckoutCreate

from django.urls import path

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path("lesson/create", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>", LessonRetriveAPIView.as_view(), name="lesson-get"),
    path("lesson/update/<int:pk>", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lesson/delete/<int:pk>", LessonDestroyAPIView.as_view(), name="lesson-delete"),
    path("cource/products/create/<int:pk>", CourceProductCreate, name="cource-products-create"),
    path("cource/prices/create/<str:product_key>/", CourcePriceCreate, name="cource-prices-create"),
    path("cource/checkout/create/<str:price_key>", CourceCheckoutCreate, name="cource-checkout-create"),
]+router.urls
