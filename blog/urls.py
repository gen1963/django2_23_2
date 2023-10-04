from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("blog/", views.index, name="main"),
    path("blog/post<title>", views.post, name="post"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contacts", views.contacts, name="contacts"),
    path('blog/category/<int:id>', views.category, name='category'),
    path('blog/search/', views.search, name="search"),
    path('blog/create/', views.create, name='create'),
    # path('blog/post<int:pk>', views.comments_post, name='Comments_post'),
    path('review/<int:pk>', views.post_com, name='block_review'),
    # path('blog/post<int:pk>', views.post_com, name='block_review'),
    path("blog/login/", LoginView.as_view(), name="blog_login"),
    path("blog/logout/", LogoutView.as_view(), name="blog_logout"),
    path('blog/profile/', views.profile, name="profile"),
    path('blog/register/', views.register, name='register')
    # path("<dynamic_url>, views.pro_url, name="test"),

]

