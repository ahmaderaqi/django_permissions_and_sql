from django.urls import path
from .views import ThingList,ThingDetail,postDetail,PostList
urlpatterns = [
    path('/', ThingList.as_view(),name='thing_list'),
    path('/<int:pk>/',ThingDetail.as_view(),name='thing_detail'),
    path('/post/', PostList.as_view(),name='post_list'),
    path('/post/<int:pk>/',postDetail.as_view(),name='post_detail')
    

]