from django.urls import path
from . import views
from .views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('download_pdf/', views.download_pdf, name="download_pdf"),
]