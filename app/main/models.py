from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Catcamas(models.Model):
	seccion = models.CharField(max_length=765, db_column='seccion', blank=True) 
	cama = models.CharField(max_length=765, db_column='cama', blank=True) 
	class Meta:
		db_table = 'ca_camas'

class Catcie(models.Model):
	clave = models.CharField(max_length=765, db_column='clave', blank=True) 
	nombre = models.CharField(max_length=765, db_column='nombre', blank=True) 
	class Meta:
		db_table = 'cie_10'

class Catocupacion(models.Model):
	ocupacion = models.CharField(max_length=765, db_column='ocupacion', blank=True) 
	class Meta:
		db_table = 'ca_ocupacion'

class Catedocivil(models.Model):
	estado_civil = models.CharField(max_length=765, db_column='estado_civil', blank=True) 
	class Meta:
		db_table = 'ca_estado_civil'

class Catescolaridad(models.Model):
	escolaridad = models.CharField(max_length=765, db_column='escolaridad', blank=True) 
	class Meta:
		db_table = 'ca_escolaridad'

class Catestados(models.Model):
	estado = models.CharField(max_length=765, db_column='nombre', blank=True) 
	class Meta:
		db_table = 'ca_estados'

class Catreligion(models.Model):
	religion = models.CharField(max_length=765, db_column='religion', blank=True) 
	class Meta:
		db_table = 'ca_religion'

class Identificacion(modesls.Model):
	afiliacion = models.CharField(max_length=200, db_column='afiliacion', blank=True)
	nombre = models.CharField(max_length=200, db_column='afiliacion', blank=True)
	genero = models.CharField(max_length=20, db_column='afiliacion', blank=True)
	edad = models.CharField(max_length=5, db_column='afiliacion', blank=True)
	ocupacion = models.ForeignKey(Catocupacion, db_column='id_ocupacion', blank=True)
	estado_civil = models.ForeignKey(Catedocivil, db_column='id_edo_civil', blank=True)
	escolaridad = models.ForeignKey(Catescolaridad, db_column='id_escolaridad', blank=True)
	fecha_nacimiento = models.DateField(db_column='fecha_nacimietno', blank=True)
	a_nacimietno = models.CharField(max_length=5, db_column='a_nacimiento', blank=True)
	lugar_nacimiento = models.ForeignKey(Catestados, db_column='id_estados', blank=True)
	lugar_residencia = models.ForeignKey(Catestados, db_column='id_estados', blank=True)
	religion = models.ForeignKey(Catreligion, db_column='id_religion', blank=True)

	class Meta:
		db_table = 'identificacion'


class Pacientecama(models.Model):
	paciente = models.ForeignKey(Catreligion, db_column='id_identificacion', blank=True)
	cama = models.ForeignKey(Catreligion, db_column='id_identificacion', blank=True)

	class Meta:
		db_table = 'paciente_cama'