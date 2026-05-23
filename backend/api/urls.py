from django.urls import path
from users import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
   path('register/', UserViews.RegisterView.as_view()),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # access tokens
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # refresh tokens
   path('profile/', UserViews.ProfileView.as_view()), # user profile
]
