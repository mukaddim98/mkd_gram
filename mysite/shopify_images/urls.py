from django.urls import path

from . import views

app_name = 'shopify_images'
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('my_images/', views.myImagesPage, name="my_images"),
    path('success/', views.success, name='success'),
]