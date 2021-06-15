from django.urls import path
from .views import SignupPage, ResultsList, UploadTemplateView, csv_upload_view
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', SignupPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ResultsList.as_view(), name='results'),
    path('upload/', csv_upload_view, name='upload'),
    path('upload_new_results/', UploadTemplateView.as_view(), name='upload_objects'),
]

