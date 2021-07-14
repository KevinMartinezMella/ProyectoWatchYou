import pywhatkit
from datetime import datetime
class Msg:
    def __init__(self):
        self.now = datetime.now()
        self.numero = "953485258"
    def mensaje(self):
        msg = "Saludos Jean, se han verificado las conexiones el %02d/%02d/%04d:%2d:%02d:%02d " % (self.now.day,self.now.month,self.now.year,self.now.hour,self.now.minute,self.now.second)