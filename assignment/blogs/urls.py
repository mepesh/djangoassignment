from django.urls import path
from .views import*

urlpatterns = [
    path('list/', list_post),
    path('post/', post),
    path('', home)
]
