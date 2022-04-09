from django.urls import path
from .views import *

urlpatterns = [
    path('admin/category/', CategoryListView.as_view(), name='category' ),
    path('admin/add-category/', CategoryAddView.as_view(), name='add-category'),
    path('admin/update-category/<int:pk>/', CategoryUpdateView.as_view(), name='update-category'),
    path('admin/delete-category/<int:pk>/', CategoryDeleteView.as_view(), name='delete-category'),
    path('admin/post/', PostListView.as_view(), name='post' ),
    path('admin/add-post/', PostAddView.as_view(), name='add-post'),
    path('admin/update-post/<int:pk>/', PostUpdateView.as_view(), name='update-post'),
    path('admin/delete-post/<int:pk>/', PostDeleteView.as_view(), name='delete-post'),
    path('', BlogListView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='all-post'),
    path('blog/get/<int:pk>/', BlogGetListView.as_view(), name='get-blog'),
]
