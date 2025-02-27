from django.contrib import admin
from django.urls import path
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('signup/', views.signup, name='signup'),
    path('loginn/', views.loginn, name='loginn'),
    path('home/', views.home, name='home'),
    path('add-posts/', views.newPost, name='add_post'),
    path('my-posts/', views.myPost, name='my_posts'),
    path('logout/', views.signout, name='logout'),
]
