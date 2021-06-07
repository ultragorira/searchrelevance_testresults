from django.urls import path
from .views import CustomLoginView, SignupPage, ResultsList
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', SignupPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ResultsList.as_view(), name='results')
]