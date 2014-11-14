# -*- coding: utf-8 -*-

from django.test import TestCase
from estacionamientos.forms import *
import datetime
# Create your tests here.

class MyTests(TestCase):
###################################################################
# ESTACIONAMIENTO_EXTENDED_FORM
###################################################################

	def test_EstacionamientoExtendedForm_UnCampo(self):
		form_data = { 'puestos': 2}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_DosCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_TresCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_CuatroCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_CincoCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_TodosCamposBien(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),True)
		
	def test_EstacionamientoExtendedForm_TodosCamposBien(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),True)
		
	def test_EstacionamientoExtendedForm_Puestos0(self):
		form_data = { 'puestos': 0,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),True)
		
	def test_EstacionamientoExtendedForm_HoraInicioIgualHoraCierre(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(6,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),True)
		
	def test_EstacionamientoExtendedForm_HoraIniReserIgualHoraFinReser(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(7,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),True)
		
	def test_EstacionamientoExtendedForm_StringEnPuesto(self):
		form_data = { 'puestos': 'hola',
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_StringHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_NumeroNegativoHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin': -1,
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_NoneEntarifa(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': datetime.time(14,0),
								'tarifa': None}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_NoneEnHorarioReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': datetime.time(19,0),
								'horario_reserin': None,
								'horario_reserout': datetime.time(14,0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)
		
	def test_EstacionamientoExtendedForm_listaEnHoraReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6,0),
								'horarioout': datetime.time(19,0),
								'horario_reserin': datetime.time(7,0),
								'horario_reserout': [datetime.time(14,0)],
								'tarifa': 12}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(),False)