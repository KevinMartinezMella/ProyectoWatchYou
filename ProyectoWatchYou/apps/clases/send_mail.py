import smtplib

class Email:

    def sendMail(self,input):
        from_addr = 'yonibanck@gmail.com'
        to = ['jeanpaoloramos@gmail.com','iamkamm7@gmail.com','dosorno@codingdojo.cl']
        sub = 'Resultados revision programada de equipos'
        mes = " ".join(input)
        message = 'Subject: {}\n\n{}'.format(sub, mes)
        username = 'yonibanck@gmail.com'
        password = 'Itachi_16'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, to, message)
        server.quit()