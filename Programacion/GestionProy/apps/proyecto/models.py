from django.db import models

# Create your models here.

class Rol (models.Model):
	id_rol=models.AutoField(primary_key= True)
	descripcion=models.CharField(max_length=50 ,blank = False , null =False)
	permiso= models.CharField(max_length=100)
	
	def __str__(self):
		return self.descripcion
	
class Proyecto (models.Model):
	opcionfa=(('Analisis','Analisis'),('Diseño','Diseño'),('Desarrollo','Desarrollo'),('Mantenimiento','Mantenimiento'),('Prueba','Prueba'))
	opciones=(('P','Pendiente'),('C','Cancelado'),('F','Finalizado'))
	
	id_proyecto =models.AutoField(primary_key = True)
	nombre= models.CharField(max_length=50 ,blank = False , null =False)
	objetivo = models.CharField(max_length=50 ,blank = False , null =False)
	fecha_ini=models.DateField(blank=False ,null= False)
	fecha_fin = models.DateField(blank=True ,null= True)
	estado =models.CharField(max_length=50 ,blank = False , null =False,choices =opciones)
	fase=models.CharField(max_length=50,choices=opcionfa)
	
	
	def __str__(self):
		return self.nombre
		

class Usuario (models.Model):
	cedula = models.IntegerField (primary_key = True)
	nombre= models.CharField(max_length=50 ,blank = False , null =False)
	apellido = models.CharField(max_length=50 ,blank = False , null =False)
	fecha_nac =models.DateField(blank=False ,null= False)
	direccion =models.CharField(max_length=50 ,blank = False , null =False)
	telefono = models.CharField(max_length=50 ,blank = False , null =False)
	user_name = models.CharField(max_length=50 ,blank = False , null =False)
	password = models.CharField(max_length=50 ,blank = False , null =False)
	cod_rol =models.ForeignKey(Rol, on_delete=models.CASCADE,blank= True,null=True)
	proyecto=models.OneToOneField(Proyecto,on_delete=models.CASCADE,blank= True,null=True)
	
	def __str__(self):
		return self.nombre
	

	
class LineaBase (models.Model):
	opcion =(('Abierto','Abierto'),('Cerrado','Cerrado'))
	
	id_lb=models.AutoField(primary_key = True)
	proyecto=models.OneToOneField(Proyecto, on_delete=models.CASCADE, blank= True,null=True)
	descripcion=models.CharField(max_length=50 ,blank = True , null =True)
	estado=models.CharField(choices=opcion,max_length=50 ,blank = False , null =False)
	
	def __str__(self):
		return self.descripcion

class Item (models.Model):
	opcion =(('Pendiente','Pendiente'),('Cancelado','Cancelado'),('Finalizado','Finalizado'))
	pri =(('Alta','Alta'),('Media','Media'),('Baja','Baja'))
	id_item =models.AutoField(primary_key = True)
	version=models.CharField(max_length=50 ,blank = False , null =False)
	estado=models.CharField(max_length=50 ,blank = False , null =False,choices=opcion)
	descripcion=models.CharField(max_length=50 ,blank = False , null =False)
	dependencia=models.CharField(max_length=50 ,blank = True)
	prioridad= models.CharField(max_length=50 ,blank = True, choices= pri)
	fecha_ini=models.DateField(blank=False ,null= False)
	fecha_mod=models.DateTimeField(blank=True ,null=True)
	observacion=models.CharField(max_length=50 ,blank =True)
	linea_base=models.ForeignKey(LineaBase, on_delete=models.CASCADE,blank= True,null=True)
	proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE,blank= True,null=True)
	user=models.ForeignKey(Usuario, on_delete=models.CASCADE,blank= True,null=True)
	
	
	def __str__(self):
		return self.descripcion
	