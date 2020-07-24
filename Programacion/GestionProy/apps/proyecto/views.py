from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from apps.proyecto.form import ProyectoForm,UsuarioForm,ItemForm,LineaBaseForm
from apps.proyecto.models import Proyecto,Usuario,Item,LineaBase
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


def Home(request):

	items=Item.objects.all()
	usuarios=Usuario.objects.all()
	return render(request,'proyecto/indexhome.html',{'usuarios':usuarios,'items':items})
	
#Procesos de Proyecto	

def BuscarProyecto(request):
	
	if request.method == 'GET':
		query= request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if query is not None:
            #lookups= Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)
			results= Proyecto.objects.filter(Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)| 
			Q(estado__icontains=query)|Q(fase__icontains=query)|Q(fecha_ini__icontains=query) | Q(fecha_fin__icontains=query)).distinct()
			context={'results': results,'submitbutton': submitbutton}
			return render(request,'proyecto/buscarproy.html',context)

		else:
			return render(request,'proyecto/buscarproy.html')

	else:
		return render(request,'proyecto/buscarproy.html')
		
def BuscarModProyecto(request):
	
	if request.method == 'GET':
		query= request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if query is not None:
            #lookups= Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)
			results= Proyecto.objects.filter(Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)| 
			Q(estado__icontains=query)|Q(fase__icontains=query)|Q(fecha_ini__icontains=query) | Q(fecha_fin__icontains=query)).distinct()
			context={'results': results,'submitbutton': submitbutton}
			return render(request,'proyecto/buscarmodproy.html',context)

		else:
			return render(request,'proyecto/buscarmodproy.html')

	else:
		return render(request,'proyecto/buscarmodproy.html')

	
def PagPrincipal(request):
    return render(request,'proyecto/index.html')

def ProyectoView(request):
	if request.method =='POST':
		proy_form= ProyectoForm(request.POST)
		if proy_form.is_valid():
			proy_form.save()
			return redirect('proyecto:Principal')
	else:
		proy_form=ProyectoForm()
	return render(request,'proyecto/proyectoform.html',{'proy_form':proy_form})
	
	
def ListarProyecto(request):
	proyectos= Proyecto.objects.all()
	return render(request,'proyecto/listaproyecto.html',{'proyectos':proyectos})
	
	
	
	
def ModProyecto(request):
	proyectos= Proyecto.objects.all()
	return render(request,'proyecto/modproy.html',{'proyectos':proyectos})
	
def EditarProyecto(request,id):

	error=None
	proy_form=None
	try:
		proy= Proyecto.objects.get(id_proyecto=id)
		
		if request.method =='GET' :
			proy_form=ProyectoForm(instance = proy)
		else:
			proy_form = ProyectoForm(request.POST ,instance= proy)
			if proy_form.is_valid():
				proy_form.save()
			return redirect('proyecto:Principal')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'proyecto/proyectoform.html',{'proy_form':proy_form, 'error':error})
	
	
	
def EliminarProyecto(request,id):
	proy=Proyecto.objects.get(id_proyecto=id)
	if request.method =='POST':
		proy.delete()
		return redirect('proyecto:listar_proy')
	return render(request,'proyecto/elimproyecto.html',{'proy':proy})
	
	
	
#Procesos de Usuario

def PagPrincipalUsuario(request):
    return render(request,'proyecto/indexuser.html')

def UsuarioView(request):
	if request.method =='POST':
		usuario_form= UsuarioForm(request.POST)
		if usuario_form.is_valid():
			usuario_form.save()
			return redirect('proyecto:PrincipalUsuario')
	else:
		usuario_form=UsuarioForm()
	return render(request,'proyecto/usuarioform.html',{'usuario_form':usuario_form})


def ListarUsuarios(request):
	usuarios= Usuario.objects.all()
	return render(request,'proyecto/listausuario.html',{'usuarios':usuarios})
	
	
def EditarUsuario(request,id):

	error=None
	usuario_form=None
	try:
		usuario= Usuario.objects.get(cedula=id)
		
		if request.method =='GET' :
			usuario_form=UsuarioForm(instance = usuario)
		else:
			usuario_form = UsuarioForm(request.POST ,instance= usuario)
			if usuario_form.is_valid():
				usuario.save()
			return redirect('proyecto:PrincipalUsuario')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'proyecto/usuarioform.html',{'usuario_form':usuario_form, 'error':error})
	
def EliminarUsuario(request,id):
	usuario=Usuario.objects.get(cedula=id)
	if request.method =='POST':
		usuario.delete()
		return redirect('proyecto:listar_user')
	return render(request,'proyecto/elimusuario.html',{'usuario':usuario})
	
	
def BuscarUsuario(request):
	
	if request.method == 'GET':
		query= request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if query is not None:
            #lookups= Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)
			results= Usuario.objects.filter(Q(cedula__icontains=query) | Q(nombre__icontains=query)| 
			Q(apellido__icontains=query)|Q(cod_rol__descripcion__icontains=query)|Q(proyecto__nombre__icontains=query)).distinct()
			context={'results': results,'submitbutton': submitbutton}
			return render(request,'proyecto/buscaruser.html',context)

		else:
			return render(request,'proyecto/buscaruser.html')

	else:
		return render(request,'proyecto/buscaruser.html')
		
		
		
def ModUsuario(request):
	usuarios= Usuario.objects.all()
	return render(request,'proyecto/moduser.html',{'usuarios':usuarios})
	
	
def BuscarModUsuario(request):
	
	if request.method == 'GET':
		query= request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if query is not None:
            #lookups= Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)
			results= Usuario.objects.filter(Q(cedula__icontains=query) | Q(nombre__icontains=query)| 
			Q(apellido__icontains=query)|Q(cod_rol__descripcion__icontains=query)|Q(proyecto__nombre__icontains=query)).distinct()
			context={'results': results,'submitbutton': submitbutton}
			return render(request,'proyecto/buscarmoduser.html',context)

		else:
			return render(request,'proyecto/buscarmoduser.html')

	else:
		return render(request,'proyecto/buscarmoduser.html')
	
#Procesos de Item

def PagPrincipalItem(request):
    return render(request,'proyecto/indexitem.html')
	
def ItemView(request):
	if request.method =='POST':
		item_form= ItemForm(request.POST)
		if item_form.is_valid():
			item_form.save()
			return redirect('proyecto:PrincipalItem')
	else:
		item_form=ItemForm()
	return render(request,'proyecto/itemform.html',{'item_form':item_form})

def ListarItem(request):
	items= Item.objects.all()
	return render(request,'proyecto/listaitem.html',{'items':items})
	
	
def EditarItem(request,id):

	error=None
	item_form=None
	try:
		item= Item.objects.get(id_item=id)
		
		if request.method =='GET' :
			item_form=ItemForm(instance = item)
		else:
			item_form = ItemForm(request.POST ,instance= item)
			if item_form.is_valid():
				item_form.save()
			return redirect('proyecto:PrincipalItem')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'proyecto/itemform.html',{'item_form':item_form, 'error':error})
	
	
def EliminarItem(request,id):
	item=Item.objects.get(id_item=id)
	if request.method =='POST':
		item.delete()
		return redirect('proyecto:listar_item')
	return render(request,'proyecto/elimitem.html',{'item':item})
	
	
def BuscarItem(request):
	
	if request.method == 'GET':
		query= request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if query is not None:
            #lookups= Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)
			results= Item.objects.filter(Q(id_item__icontains=query) | Q(estado__icontains=query)| 
			Q(prioridad__icontains=query)|Q(descripcion__icontains=query)|Q(fecha_ini__icontains=query) 
			| Q(linea_base__descripcion__icontains=query)| Q(user__nombre__icontains=query)| Q(proyecto__nombre__icontains=query)).distinct()
			context={'results': results,'submitbutton': submitbutton}
			return render(request,'proyecto/buscaritem.html',context)

		else:
			return render(request,'proyecto/buscaritem.html')

	else:
		return render(request,'proyecto/buscaritem.html')


def ModItem(request):
	items= Item.objects.all()
	return render(request,'proyecto/moditem.html',{'items':items})
	
	
	
def BuscarModItem(request):
	
	if request.method == 'GET':
		query= request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if query is not None:
            #lookups= Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)
			results= Item.objects.filter(Q(id_item__icontains=query) | Q(estado__icontains=query)| 
			Q(prioridad__icontains=query)|Q(descripcion__icontains=query)|Q(fecha_ini__icontains=query) 
			| Q(linea_base__descripcion__icontains=query)| Q(user__nombre__icontains=query)| Q(proyecto__nombre__icontains=query)).distinct()
			context={'results': results,'submitbutton': submitbutton}
			return render(request,'proyecto/buscarmoditem.html',context)

		else:
			return render(request,'proyecto/buscarmoditem.html')

	else:
		return render(request,'proyecto/buscarmoditem.html')

	
#Procesos de Linea Base

def PagPrincipalLB(request):
    return render(request,'proyecto/indexlb.html')
	
	
def LBView(request):
	if request.method =='POST':
		lb_form= LineaBaseForm(request.POST)
		if lb_form.is_valid():
			lb_form.save()
			return redirect('proyecto:PrincipalLB')
	else:
		lb_form=LineaBaseForm()
	return render(request,'proyecto/lineabaseform.html',{'lb_form':lb_form})
	
def ListarLB(request):
	lbs= LineaBase.objects.all()
	return render(request,'proyecto/listalb.html',{'lbs':lbs})
	
	
def BuscarLB(request):
	
	if request.method == 'GET':
		query= request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if query is not None:
            #lookups= Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)
			results= LineaBase.objects.filter(Q(id_lb__icontains=query) | Q(proyecto__nombre__icontains=query)| Q(descripcion__icontains=query) | Q(estado__icontains=query)).distinct()
			context={'results': results,'submitbutton': submitbutton}
			return render(request,'proyecto/buscarlb.html',context)

		else:
			return render(request,'proyecto/buscarlb.html')

	else:
		return render(request,'proyecto/buscarlb.html')
		
def BuscarModLB(request):
	
	if request.method == 'GET':
		query= request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if query is not None:
            #lookups= Q(id_proyecto__icontains=query) | Q(nombre__icontains=query)
			results= LineaBase.objects.filter(Q(id_lb__icontains=query) | Q(proyecto__nombre__icontains=query)| Q(descripcion__icontains=query) | Q(estado__icontains=query)).distinct()
			context={'results': results,'submitbutton': submitbutton}
			return render(request,'proyecto/buscarmodlb.html',context)

		else:
			return render(request,'proyecto/buscarmodlb.html')

	else:
		return render(request,'proyecto/buscarmodlb.html')
	
def EditarLB(request,id):

	error=None
	lb_form=None
	try:
		lb= LineaBase.objects.get(id_lb=id)
		
		if request.method =='GET' :
			lb_form=LineaBaseForm(instance = lb)
		else:
			lb_form = LineaBaseForm(request.POST ,instance= lb)
			if lb_form.is_valid():
				lb_form.save()
			return redirect('proyecto:PrincipalLB')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'proyecto/lineabaseform.html',{'lb_form':lb_form, 'error':error})



def EliminarLB(request,id):
	lb=LineaBase.objects.get(id_lb=id)
	if request.method =='POST':
		lb.delete()
		return redirect('proyecto:listar_lb')
	return render(request,'proyecto/elimlb.html',{'lb':lb})
	
	
	
def ModLB(request):
	lbs= LineaBase.objects.all()
	return render(request,'proyecto/modlb.html',{'lbs':lbs})
	
	


		
	
	