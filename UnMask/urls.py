
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('login/', views.loginPage, name="login"), 
  path('register/', views.registerPage, name="register"),
  path('match/', views.matchPage, name="match"),
  path('profile/', views.profilePage, name="profile"),
  path('chat/', views.chatPage, name="chat"),
  
  



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)