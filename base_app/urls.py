from django.urls import path
from base_app.views import index

urlpatterns = [
    path('', index, name='index'),
]