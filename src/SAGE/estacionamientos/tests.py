# -*- coding: utf-8 -*-


# Create your tests here.
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test import Client
from estacionamientos.forms import *
import unittest

###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################

class SimpleTest(unittest.TestCase):
	def setUp(self):
		self.client = Client()

	def test_primera(self):
		response = self.client.get('/estacionamientos/')
		self.assertEqual(response.status_code, 200)



###################################################################
#                    ESTACIONAMIENTO_ALL FORM
###################################################################

class SimpleFormTestCase(TestCase):

	def test_CamposVacios(self):
		form_data = {}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)
	def test_SoloUnCampoNecesario(self):
		form_data = {
			'propietario': 'Pedro'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)
	def test_DosCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)
	def test_TresCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)

	def test_TodosLosCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),True)

	def test_PropietarioInvalidoDigitos(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)

	def test_PropietarioInvalidoSimbolos(self):
		form_data = {
			'propietario': 'Pedro!',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)

	def test_RIFtamanoinvalido(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V1234567'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)

	def test_RIFformatoinvalido(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'Kaa123456789'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)

	def test_AgregarTLFs(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),True)

	def test_FormatoInvalidoTLF(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02119322878'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)
	
	def test_TamanoInvalidoTLF(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '0219322878'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)

	def test_AgregarCorreos(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878',
			'email_1': 'adminsitrador@admin.com',
			'email_2': 'usua_rio@users.com'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),True)

	def test_CorreoInvalido(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878',
			'email_1': 'adminsitrador@a@dmin.com'
		}
		form = EstacionamientoForm(data=form_data)
		self.assertEqual(form.is_valid(),False)

#class MyTest(unittest.TestCase):
#	def setUp(self):
#		self.client = Client()

#	def test_segunda(self):
#		response = self.client.post('/estacionamientos/', {})
#		print response.status_code
		#self.assertEqual(response.status_code, 200)
#		self.assertFormError(response, 'form', 'some_field', 'This field is required.')
		#response = c.post('/estacionamientos/', {'propietario': 'Victor', 'nombre': 'Destiny', 'direccion': 'Caracas', 'rif': 'V123456789'})
		#response.status_code