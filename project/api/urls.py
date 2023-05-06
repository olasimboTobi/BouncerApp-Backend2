from api.views import *
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('otp/verify/', VerifyOTPView.as_view(), name='verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', SetNewPasswordAPIView.as_view(), name='reset-password'),
    path('product/', ProductListView.as_view(), name='product'),

]
