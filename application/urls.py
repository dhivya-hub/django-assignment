from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('', home),
    path('teacher/', teacher_detail),
    path('student/', student_detail),
    path('teacher_one/<int:id>/', teacher_one),
    path('teacher_update/<int:id>/', teacher_update),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]