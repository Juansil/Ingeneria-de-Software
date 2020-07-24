from django import forms
from apps.proyecto.models import Proyecto,Usuario,Item,LineaBase

class ProyectoForm(forms.ModelForm):
	class Meta :
		model= Proyecto
		fields=[
		'id_proyecto',
		'nombre',
		'objetivo', 
		'fecha_ini',
		'fecha_fin',
		'estado',
		'fase',]
		
		labels = {
		'nombre':'Nombre del Proyecto',
		'objetivo':'Objetivo', 
		'fecha_ini':'Fecha de inicio',
		'fecha_fin':'Fecha de culmicion',
		'estado':'Estado',
		'fase':'Fase',
		
		}
		
		
		widgets={
		'id_proyecto': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese ID'}),
		'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre del Proyecto','style':'width:650px'}),
		'objetivo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el Objetivo del Proyecto','style':'width:650px'}), 
		'fecha_ini': forms.DateInput(attrs={'class':'form-control','placeholder':'Ingrese Fecha de Inicio','style':'width:650px'}),
		'fecha_fin': forms.DateInput(attrs={'class':'form-control','placeholder':'Ingrese Fecha Finalizacion','style':'width:650px'}),
		'estado': forms.Select(attrs={'class':'form-control','placeholder':'Pendiente/Finalizado/Cancelado','style':'width:650px'}),
		'fase':forms.Select(attrs={'class':'form-control','placeholder':'Diseño/Desarrollo/Prueba/Mantenimiento/Analisis','style':'width:650px'}),
		
		}
		
		
class UsuarioForm(forms.ModelForm):
	class Meta :
		model= Usuario
		fields=[
		'cedula',
		'nombre',
		'apellido', 
		'fecha_nac',
		'direccion',
		'telefono',
		'user_name',
		'password',
		'cod_rol',
		'proyecto',
		]
		
		labels = {
			'cedula':'N° de Cedula',
			'nombre':'Nombre/s',
			'apellido':'Apellido/s', 
			'fecha_nac':'Fecha de Nacimiento',
			'direccion':'Direccion',
			'telefono':'Telefono',
			'user_name':'User Name',
			'password':'Password',
			'cod_rol':'Rol',
			'proyecto':'Proyecto',
			}
			
			
		widgets={
			'cedula': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Numero de CI','style':'width:650px'}),
			'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese  Nombre','style':'width:650px'}),
			'apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido','style':'width:650px'}), 
			'fecha_nac':forms.DateInput(attrs={'class':'form-control','placeholder':'Ingrese Fecha de Nacimiento ','style':'width:650px'}),
			'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Direccion','style':'width:650px'}),
			'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un numero de telefono','style':'width:650px'}),
			'user_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Crea un Nombre de Usuario','style':'width:650px'}),
			'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Crea una contraseña','style':'width:650px'}),
			'cod_rol':forms.RadioSelect(attrs={'style':'width:50px'}),
			'proyecto':forms.Select(attrs={'class':'form-control','placeholder':'Ingrese su Nombre','style':'width:650px'}),
			}
		
class ItemForm(forms.ModelForm):
	class Meta :
		model= Item
		fields=[
		'id_item',
		'version',
		'estado', 
		'descripcion',
		'dependencia',
		'prioridad',
		'fecha_ini',
		'fecha_mod',
		'observacion',
		'linea_base',
		'proyecto',
		'user',]
		
		
		label ={
		'version':'Version',
		'estado':'Estado', 
		'descripcion':'Descripcion',
		'dependencia':'Dependencia',
		'prioridad':'Prioridad',
		'fecha_ini':'Fecha_inicio',
		'fecha_mod':'Fecha_modificacion',
		'observacion':'Observacion',
		'linea_base':'Seleccione la Linea Base',
		'proyecto':'Seleccione el Proyecto',
		'user':'Seleccione el Usuario',
		}
		
		
		widgets ={
		'version':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la version del item','style':'width:650px'}),
		'estado':forms.Select(attrs={'class':'form-control','placeholder':'Ingrese su Nombre','style':'width:650px'}), 
		'descripcion':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese una descripcion para el item','style':'width:650px'}),
		'dependencia':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su dependencia','style':'width:650px'}),
		'prioridad':forms.Select(attrs={'class':'form-control','placeholder':'Seleccione un Proyecto','style':'width:650px'}),
		'fecha_ini':forms.DateInput(attrs={'class':'form-control','placeholder':'Ingrese Fecha de Inicio ','style':'width:650px'}),
		'fecha_mod':forms.DateInput(attrs={'class':'form-control','placeholder':'Ingrese Fecha de Modificacion ','style':'width:650px'}),
		'observacion':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese una observacion de los cambios realizados','style':'width:650px'}),
		'linea_base':forms.Select(attrs={'class':'form-control','placeholder':'Seleccione un Proyecto','style':'width:650px'}),
		'proyecto':forms.Select(attrs={'class':'form-control','placeholder':'Seleccione un Proyecto','style':'width:650px'}),
		'user':forms.Select(attrs={'class':'form-control','placeholder':'Seleccione un Proyecto','style':'width:650px'}),
		
		
		}
		
class LineaBaseForm(forms.ModelForm):
	class Meta:
		model= LineaBase
		fields=[
		'id_lb',
		'proyecto',
		'descripcion',
		'estado',
		]
	
	
		labels = {
		'descripcion':'Descripcion',
		'estado':'Estado', 
		'proyecto':'Proyecto',
		
		}
		
		
		
		widgets={
		'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Descripcion de Linea Base','style':'width:650px'}),
		'estado': forms.Select(attrs={'class':'form-control','placeholder':'Pendiente/Finalizado/Cancelado','style':'width:650px'}),
		'proyecto': forms.Select(attrs={'class':'form-control','placeholder':'Seleccione un Proyecto','style':'width:650px'}), 
		
		
		}
		
		
		
		
		
	
			


