from django.conf.urls import url,include
from django.urls import path
from .views import  ProyectoView,ListarProyecto,EditarProyecto,EliminarProyecto,ModProyecto,BuscarProyecto,BuscarModProyecto
from .views import UsuarioView,ListarUsuarios,EditarUsuario,EliminarUsuario,BuscarUsuario,ModUsuario,BuscarModUsuario
from .views import ItemView,ListarItem,EditarItem,EliminarItem,BuscarItem,ModItem,BuscarModItem
from.views import LBView,ListarLB,EditarLB,EliminarLB,BuscarLB,ModLB,BuscarModLB
from .views import PagPrincipal,PagPrincipalUsuario,PagPrincipalItem,PagPrincipalLB,Home
#,ListarUsuarios,EditarUsuario,EliminarUsuario


urlpatterns = [
    #url(r'^$',index, name= 'index'),
	 path('crear_proy/',ProyectoView, name ='crear_proy'),
	 path('listar_proy/',ListarProyecto, name ='listar_proy'),
	 path('editar_proy/<int:id>',EditarProyecto, name ='editar_proy'),
	 path('eliminar_proy/<int:id>',EliminarProyecto, name ='eliminar_proy'),
	 path('buscar_proy/',BuscarProyecto, name ='buscar_proy'),
	 path('buscar_mod_proy/',BuscarModProyecto, name ='buscar_mod_proy'),
	 path('mod_proy/',ModProyecto, name ='mod_proy'),
	 path('crear_user/',UsuarioView, name ='crear_user'),
	 path('listar_user/',ListarUsuarios, name ='listar_user'),
	 path('editar_user/<str:id>',EditarUsuario, name ='editar_user'),
	 path('eliminar_user/<str:id>',EliminarUsuario, name ='eliminar_user'),
	 path('buscar_user/',BuscarUsuario, name ='buscar_user'),
	 path('mod_user/',ModUsuario, name ='mod_user'),
	 path('buscar_mod_user/',BuscarModUsuario, name ='buscar_mod_user'),
	 path('crear_item/',ItemView, name ='crear_item'),
	 path('listar_item/',ListarItem, name ='listar_item'),
	 path('editar_item/<int:id>',EditarItem, name ='editar_item'),
	 path('eliminar_item/<int:id>',EliminarItem, name ='eliminar_item'),
	 path('buscar_item/',BuscarItem, name ='buscar_item'),
	 path('mod_item/',ModItem, name ='mod_item'),
	 path('buscar_mod_item/',BuscarModItem, name ='buscar_mod_item'),
	 path('crear_lb/',LBView, name ='crear_lb'),
	 path('editar_lb/<str:id>',EditarLB, name ='editar_lb'),
	 path('listar_lb/',ListarLB, name ='listar_lb'),
	 path('eliminar_lb/<int:id>',EliminarLB, name ='eliminar_lb'),
	 path('buscar_lb/',BuscarLB, name ='buscar_lb'),
	 path('mod_lb/',ModLB, name ='mod_lb'),
	 path('buscar_mod_lb/',BuscarModLB, name ='buscar_mod_lb'),
	 path('inicio/',Home,name ='inicio'),
	 path('Principal/', PagPrincipal ,name ='Principal'),
	 path('PrincipalUsuario/', PagPrincipalUsuario ,name ='PrincipalUsuario'),
	 path('PrincipalItem/', PagPrincipalItem ,name ='PrincipalItem'),
	 path('PrincipalLB/', PagPrincipalLB ,name ='PrincipalLB'),
]