import pyttsx3
import platform
import subprocess
import os as op
from send_mail import Email
from datetime import datetime
from pyttsx3 import engine
#from apps.servidores.models import Servidor


class Monitor:
	def __init__(self):
		#self.host = Servidor.objects.all()
		self.host = ['www.google.com']
	
	def ping(self):
		for i in range(0,len(self.host)):
			os = "-n" if platform.system().lower() == "windows" else "-c"
			action = ['ping', os,'5', self.host[i]]
			subprocess.call(action)
			p = subprocess.Popen('ping '+self.host[i],stdout=subprocess.PIPE)
			p.wait()
		if p.poll():
			print(self.host[i]+" is Down")
			stat = False
		else:
			print(self.host[i]+" is Up")
			stat = True

		return stat
	
ejecutar = Monitor()
ejecutar.ping()

class Validar:

	def __init__(self):
		self.engine = pyttsx3.init()
		self.engine.setProperty('rate',300)

	def verificar(self):
		data = Monitor()
		self.engine.setProperty('rate',300)
		if ejecutar:
			print("Equipos operativos")
			self.engine.say("Funciona")
			self.engine.runAndWait()
			new_email = Email()
			new_email.sendMail(data.host)

		else:
			print("Equipo Caido")
			self.engine.say("Hubo un fallo")
			self.engine.runAndWait()

		return self

realizar_validacion = Validar()
realizar_validacion.verificar()
