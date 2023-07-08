from django.shortcuts import render
from rest_framework import generics
from .models import Thing,Post
from .serializer import ThingSerializer,PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

# view//get
# class ThingList(generics.ListAPIView):
#     queryset =Thing.objects.all()
#     serializer_class=ThingSerializer

# create a new thing
class ThingList(generics.ListCreateAPIView):
    queryset =Thing.objects.all()
    serializer_class=ThingSerializer
    permission_classes = [IsAuthenticated]

# class ThingDetail(generics.RetrieveAPIView):
#     queryset =Thing.objects.all()
#     serializer_class=ThingSerializer

# update
# class ThingDetail(generics.RetrieveUpdateAPIView):
#     queryset =Thing.objects.all()
#     serializer_class=ThingSerializer

# delete
class ThingDetail(generics.RetrieveDestroyAPIView):
    queryset =Thing.objects.all()
    serializer_class=ThingSerializer
    permission_classes = [IsAuthenticated]



# posts

# create a new thing
class PostList(generics.ListCreateAPIView):
    queryset =Post.objects.all()
    serializer_class=PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

# class postDetail(generics.RetrieveAPIView):
#     queryset =Thing.objects.all()
#     serializer_class=PostSerializer

# update
# class postDetail(generics.RetrieveUpdateAPIView):
#     queryset =Thing.objects.all()
#     serializer_class=PostSerializer

# delete
class postDetail(generics.RetrieveDestroyAPIView):
    queryset =Thing.objects.all()
    serializer_class=PostSerializer
    permission_classes = [AllowAny]