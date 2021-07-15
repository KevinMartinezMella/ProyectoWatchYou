import pyttsx3
import platform
import subprocess
import os as op
from apps.clases.send_mail import Email
#from apps.clases.send_wsp import Msg
from datetime import datetime
from pyttsx3 import engine
from apps.servidores.models import Servidor


class Monitor:
	def __init__(self):
		self.host = Servidor.objects.all()
	# 	self.idserver = ""
	# 	#self.host = ['www.google.com']
	
	def ping(self,idserver=""):
		if len(idserver) > 0 or idserver != "":
			self.host = Servidor.objects.get(id=idserver)
			os = "-n" if platform.system().lower() == "windows" else "-c"
			action = ['ping', os,'5', self.host.ip]
			subprocess.call(action)
			p = subprocess.Popen('ping '+self.host.ip,stdout=subprocess.PIPE)
			p.wait()
			global nombre
			nombre = self.host.nombre_servidor
		else:
			self.host = Servidor.objects.all()
			for i in self.host:
				os = "-n" if platform.system().lower() == "windows" else "-c"
				action = ['ping', os,'5', i.ip]
				subprocess.call(action)
				p = subprocess.Popen('ping '+i.ip,stdout=subprocess.PIPE)
				p.wait() 
				nombre = i.nombre_servidor
				if p.poll():
					print(i.nombre_servidor+" is Down")
					stat = False
				else:
					print(i.nombre_servidor+" is Up")
					stat = True

			return stat
	
ejecutar = Monitor()
ejecutar.ping()

class Validar:

	def __init__(self):
		self.engine = pyttsx3.init()
		self.engine.setProperty('rate',300)

	def verificar(self):
		if ejecutar:
			print("Equipos operativos")
			new_email = Email()
			new_email.sendMail(nombre+" Is Up")
			# new_message = Msg()
			# new_message.mensaje(nombre)
			# self.engine.say("Funciona")
			# self.engine.runAndWait()

		else:
			print("Equipo Caido")
			self.engine.say("Hubo un fallo")
			self.engine.runAndWait()

		return self

realizar_validacion = Validar()
realizar_validacion.verificar()
