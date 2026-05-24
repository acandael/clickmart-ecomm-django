from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from carts import views as CartViews
from products import views as ProductViews
from users import views as UserViews

urlpatterns = [
    path("register/", UserViews.RegisterView.as_view()),
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # access tokens
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # refresh tokens
    path("profile/", UserViews.ProfileView.as_view()),  # user profile
    # Category API
    path("categories/", ProductViews.CategoryListView.as_view()),
    # Category API
    path("products/", ProductViews.ProductListView.as_view()),
    # Product Detail API
    path("products/<int:pk>/", ProductViews.ProductDetailView.as_view()),
    # Carts API
    path("carts/", CartViews.CartListView.as_view()),
    path("cart/add/", CartViews.AddToCartView.as_view()),
    path("cart/items/<int:item_id>/", CartViews.ManageCartItemView.as_view()),
]
