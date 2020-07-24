from django.contrib import admin

from .models import Rol
admin.site.register(Rol)

from .models import Usuario
admin.site.register(Usuario)

from .models import Proyecto
admin.site.register(Proyecto)

from .models import LineaBase
admin.site.register(LineaBase)

from .models import Item
admin.site.register(Item)

# Register your models here.
