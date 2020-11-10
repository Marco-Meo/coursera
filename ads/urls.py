from django.urls import path

from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.all, name='all'),
    path('ad/create', views.AdCreateView.as_view(), name='create'),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(), name='update'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='detail'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
]