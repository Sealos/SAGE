from django.db import models
from apps.estacionamientos.forms import EstacionamientoForm
from apps.estacionamientos.forms import EstacionamientoextendedForm
from django.forms import ModelForm

class EstacionamientoModel(models.Model):
	
	propietario = models.CharField(max_length = 50, help_text = "Nombre Propio" )
	nombre = models.CharField(max_length = 50)
	direccion = models.TextField(max_length = 120)
	
	telefono_1 = models.CharField(blank = True, null = True, max_length = 30)
	telefono_2 = models.CharField(blank = True, null = True, max_length = 30)
	telefono_3 = models.CharField(blank = True, null = True, max_length = 30)
	
	email_1 = models.EmailField(blank=True, null=True)
	email_2 = models.EmailField(blank=True, null=True)

	rif = models.CharField(max_length = 12)
    
class EstacionamientoextendModel(models.Model):
	# ESTE CREO QUE SE TIENE QUE CAMBIAR A IntegerField 
	tarifa = models.CharField(max_length = 50)
	horarioin = models.TimeField()
	horariout = models.TimeField()
	horario_resein = models.TimeField()
	horario_reserout = models.TimeField()
	
class EstacionamientoModelForm(EstacionamientoForm):
	class Meta:
		model = EstacionamientoModel
		fields = ['propietario', 'nombre', 'direccion', 'telefono_1', 'telefono_2', 'telefono_3', 'email_1', 'email_2', 'rif']
		
class EstacionamientoextendModelForm(EstacionamientoextendedForm):
	class Meta:
		model = EstacionamientoextendModel 
		fields = ['tarifa', 'horarioin', 'horariout', 'horario_resein', 'horario_reserout']