from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.Home,name="home_url"),
    path('CreatePost/',views.PostCreateView.as_view(),name="create_post"),
    path('SinglePost/<int:pk>',views.single_post,name="single_post"),
    path('SinglePost/<int:pk>/UpdatePost/', views.PostUpdateView.as_view() ,name="update_post"),
    path('SinglePost/<int:pk>/DeletePost/', views.PostDeleteView.as_view(), name="delete_post"),
    path('Author/listview/', views.PostListView.as_view(), name="list_post"),
    path('Author/MyPOST/', views.MyPosts, name="My_post"),
    path('Reader/listview/', views.Reader_PostListView.as_view(), name="Reader_list_post"),
    path('Reader/SinglePost/<int:pk>',views.Reader_single_post,name="Reader_single_post"),
    path('Reader/SinglePosts/<int:pk>',views.Comment,name="Reader_Comment_post"),
    path('Author/SinglePosts/<int:pk>', views.Comment_Author, name="Author_Comment_post"),
]