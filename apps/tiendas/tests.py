from django.test import TestCase
from apps.tiendas.views import *
from apps.tiendas.models import Tienda,Zona
from django.test.client import RequestFactory

class ZonaMethodTests(TestCase):
	def setUp(self):
		Zona.objects.create(nombre="Zona1", localizacion="Granada",views=0,slug=0)
		Zona.objects.create(nombre="Zona2", localizacion="Cordoba",views=0,slug=0)
		print("creacion bd Zonas correcto")

	def test_Zona(self):
		zona1 = Zona.objects.get(nombre="Zona1")
		zona2 = Zona.objects.get(nombre="Zona2")
		self.assertEqual(zona1.localizacion,'Granada')
		self.assertEqual(zona2.localizacion,'Cordoba')
		print("Test Zonas correcto.")



class TiendaMethodTests(TestCase):
	def setUp(self):
		zona_1=Zona(nombre="Zona1", localizacion="Granada",views=0,slug=0)
		zona_1.save()
		zona_2=Zona(nombre="Zona2", localizacion="Cordoba",views=0,slug=0)
		zona_2.save()
		Tienda.objects.create(nombre="TiendaChana", calle="Sagrada Familia",zona=zona_1)
		Tienda.objects.create(nombre="TiendaZara", calle="Sagrada Pajaritos",zona=zona_2)
		print("creacion bd Tiendas correcto")

	def test_Tienda(self):
		tienda1 = Tienda.objects.get(nombre="TiendaChana")
		tienda2 = Tienda.objects.get(nombre="TiendaZara")
		zona1=Zona.objects.get(nombre="Zona1")
		zona2=Zona.objects.get(nombre="Zona2")
		self.assertEqual(tienda1.zona,zona1)
		self.assertEqual(tienda2.zona,zona2)
		print("Test Tiendas correcto.")