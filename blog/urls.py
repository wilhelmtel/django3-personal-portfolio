from django.urls import path
from blog import views

# the following is used to create a registered namespace for references in html.
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('trails/', views.trails, name='trails'),
    path('mytunes/', views.mytunes, name='mytunes')
    ]
