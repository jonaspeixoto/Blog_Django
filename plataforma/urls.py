from django.urls import path
from . import views
urlpatterns = [
    path('blog/', views.blog, name='blog' ),
    path('listar_post/<int:id>/', views.listar_post, name='listar_post')
]