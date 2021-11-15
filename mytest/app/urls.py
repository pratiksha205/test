from django.urls import path
from .views import download_csv, upload_csv
urlpatterns = [
    path('download/',download_csv,name='download'),
    path('upload/', upload_csv,name='upload_csv'),
]
