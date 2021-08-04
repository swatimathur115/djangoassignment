from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/',views.add_comment,name='comment'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<str:slug>/',views.CategoryView, name='category'),
    path('tag/<str:slug>/',views.TagView, name='tag'), 
    path('post/new/', views.post_new, name='post_new'),
    path('profile/', views.profile_edit, name='profile_edit'),    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/',views.logoutUSer, name='logoutUSer'),
    path('', views.post_list, name='post_list'),
]