import smtplib

class Email:

    def sendMail(self,input):
        from_addr = 'notificaciones.watchyou@gmail.com'
        to = ['jeanpaoloramos@gmail.com','iamkamm7@gmail.com']
        #to = ['jeanpaoloramos@gmail.com','iamkamm7@gmail.com','dosorno@codingdojo.cl','carolinaharispe@fondationforge.org','horacioatenas@fondationforge.org','jbalocchi@codingdojo.cl','franciscoruiz@fondationforge.cl']
        #to = ['iamkamm7@gmail.com']
        sub = 'Resultados revision programada de equipos'
        mes = str(input)
        message = 'Subject: {}\n\n{}'.format(sub, mes)
        username = 'notificaciones.watchyou@gmail.com'
        password = 'Nw..2020'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, to, message)
        server.quit()