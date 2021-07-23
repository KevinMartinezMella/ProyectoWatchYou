import pywhatkit
from datetime import datetime
class Msg:
    def __init__(self):
        self.now = datetime.now()
        self.numero = "940567702"

    def mensaje(self,input):
        host = str(input)
        msg = "Saludos Jean, se han verificado las conexiones el %02d/%02d/%04d:%2d:%02d:%02d " % (self.now.day,self.now.month,self.now.year,self.now.hour,self.now.minute,self.now.second)
        pywhatkit.sendwhatmsg(f"+56"+self.numero, "Saludos Jean, se han verificado las conexiones con "+ host +" el %02d/%02d/%04d:%2d:%02d:%02d " % (self.now.day,self.now.month,self.now.year,self.now.hour,self.now.minute,self.now.second),int(self.now.hour),int(self.now.minute+2))
