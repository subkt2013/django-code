from django.urls import path
 
from . import views
 
app_name = 'comments'
urlpatterns = [
    path('', views.CommentIndexView.as_view(), name='index'),
    path('<int:pk>/', views.ShowCommentView.as_view(), name='show'),
    path('create/', views.CreateCommentView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateCommentView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteCommentView.as_view(), name='delete'),

]