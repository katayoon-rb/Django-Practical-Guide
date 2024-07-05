from django.urls import path
from .views import StartingPageView, AllPostsView, SinglePostView, ReadLaterView

urlpatterns = [
    path('', StartingPageView.as_view(), name='starting-page'),
    path('posts/', AllPostsView.as_view(), name='posts-page'),
    path('posts/<str:slug>', SinglePostView.as_view(), name='post-detail-page'),
    path("read-later", ReadLaterView.as_view(), name="read-later")
]
 