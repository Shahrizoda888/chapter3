from django.urls import path,include
from .views import PostListView
app_name='post'
urlpatterns = [
    path('',PostListView.as_view(),name='home'),
]
