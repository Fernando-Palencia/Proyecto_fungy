
from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('login/', views.login_view, name='login'),
    path('register/', views.registro, name='register'),
    path('', views.index_view, name='index'),
    path('productos/', views.productos_view, name='productos'),
    path('paso_paso/', views.paso_paso_view, name='paso_paso'),
    path('capacitaciones/', views.capacitaciones_view, name='capacitaciones'),
    path('conocenos/', views.conocenos_view, name='conocenos'),
    path('blog/', views.blog_view, name='blog'),
    path('secret/', views.secret_view, name='secret'),
    path('logout/', views.logout_view, name='logout'),

    path('que_mas/', views.mas_view, name='que_mas'),



    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar-producto'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

