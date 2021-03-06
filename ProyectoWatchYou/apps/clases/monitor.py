from apps.estados.models import EstadoServidor
import pyttsx3
import platform
import subprocess
import os as op
from apps.clases.send_mail import Email
from apps.clases.send_wsp import Msg
from datetime import datetime
from pyttsx3 import engine
from apps.servidores.models import Servidor
from apps.estados.models import Estado


class Monitor:
	def __init__(self):
		pass
	
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
			if p.poll():
					status = ": is Down"
					print(nombre+status)
					stat = False
					server = EstadoServidor(
						servidores=self.host,
						estados = Estado.objects.get(id = 2)
					)
					server.save()
			else:
				status = ": is Up"
				print(nombre+status)
				print(nombre)
				stat = True
				server = EstadoServidor(
					servidores=self.host,
					estados = Estado.objects.get(id = 1)
				)
				server.save()

			return stat
		else:
			self.host = Servidor.objects.all()
			nombre =[]
			for i in self.host:
				os = "-n" if platform.system().lower() == "windows" else "-c"
				action = ['ping', os,'5', i.ip]
				subprocess.call(action)
				p = subprocess.Popen('ping '+i.ip,stdout=subprocess.PIPE)
				p.wait() 
				nombre.append(i.nombre_servidor)
				if p.poll():
					print(i.nombre_servidor+" is Down")
					stat = False
				else:
					print(i.nombre_servidor+" is Up")
					print(nombre)
					stat = True

			return stat
class Validar:

	def __init__(self):
		self.engine = pyttsx3.init()
		self.engine.setProperty('rate',100)

	def verificar(self, isUp):
		if isUp:
			print("Equipos operativos")
			new_email = Email()
			new_email.sendMail(str(nombre)+" Esta ok")
			new_message = Msg()
			new_message.mensaje(nombre+ ": Esta OK")
			self.engine.say("Funciona")
			self.engine.runAndWait()



		else:
			print("Equipo Caido")
			new_email = Email()
			new_email.sendMail(str(nombre)+" ESTA CAIDO")
			new_message = Msg()
			new_message.mensaje(nombre+ ": ESTA CAIDO")
			self.engine.say("Hubo un fallo")
			self.engine.runAndWait()


		return self
