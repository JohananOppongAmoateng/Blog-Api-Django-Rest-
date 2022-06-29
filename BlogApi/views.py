# Create your views here.
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .models import Post,Comments
from .serializers import PostSerializer,CommentsSerializer

class ListPostApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CreatePostApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class RetrievePostApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"
    
class UpdatePostApiView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"
    
class DestroyPostApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"

class CreateCommentsApiView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    
class UpdateCommentsApiView(UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = ["post","pk"]
    
class DestroyCommentsApiView(DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = "pk"
    


    