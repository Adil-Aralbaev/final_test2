from django.urls import path
from . import views


urlpatterns = [
    path('forum/', views.ForumListCreateAPIView.as_view()),
    path('forum/<int:pk>/', views.ForumRetrieveUpdateDestroyAPIView.as_view()),
    path('forum/<int:forum_id>/comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('forum/<int:forum_id>/comments/', views.CommentListCreateAPIView.as_view())
]

