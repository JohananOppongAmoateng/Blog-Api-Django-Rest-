
from django.urls import path
from .views import ListPostApiView,CreatePostApiView,RetrievePostApiView,DestroyCommentsApiView,DestroyPostApiView,UpdateCommentsApiView,UpdatePostApiView,CreateCommentsApiView
urlpatterns = [
   path("posts/",ListPostApiView.as_view()),
   path("post/create",CreatePostApiView.as_view()),
   path("posts/post<int:pk>/delete",DestroyPostApiView.as_view()),
   path("posts/post<int:pk>",RetrievePostApiView.as_view()),
   path("posts/post<int:pk>/update",UpdatePostApiView.as_view()),
   path("posts/post<int:post>/comments/create",CreateCommentsApiView.as_view()),
   path("comments/comment<int:pk>/update",UpdateCommentsApiView.as_view()),
   path("comments/comment<int:pk>/delete",DestroyCommentsApiView.as_view()),
]
