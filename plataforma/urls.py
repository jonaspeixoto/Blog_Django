from django.urls import path
from . import views
urlpatterns = [
    path('blog/', views.blog, name='blog' ),
    path('criar_post', views.criar_post, name='criar_post'),
    path('listar_post/<int:id>/', views.listar_post, name='listar_post'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),

]