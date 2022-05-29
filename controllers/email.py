from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


class Email:
    def __init__(self, destinatario: list, remetente: str, senha: str) -> None:
        
        """Instancia a classe com as configurações iniciais para enviar email
        Args:
            destinatario (str): uma lista com emails dos destinatarios
            remetente (str): email do remetente
            senha (str): senha do email do remetente
        """
        self.fromaddr = remetente
        self.toaddr = destinatario
        self.password = senha

    def enviar_email(self) -> None:
        """Função responsável por enviar o email.
        Anexa o arquivo pptx, criar o corpo e o assunto do email, e envia o email. 
        """
        print('Enviando email para os participantes...')
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = ' , '.join(self.toaddr)

        # Assunto do email
        msg['Subject'] = "Workmap Time GOE"
        # Corpo do emial
        body = "Olá, bem-vindo! É um prazer ter você no time. Segue em anexo o nosso Workmap."

        msg.attach(MIMEText(body, 'plain'))

        # Arquivo a ser anexado
        filename = "Workmap.pptx"
        anexo = open("/home/renata/Downloads/WorkMaptimeGOE.pptx", "rb")

        p = MIMEBase('aplication', 'octet-stream')
        p.set_payload((anexo).read())

        encoders.encode_base64(p)
        p.add_header("Content-Disposition",
                    "attachment; filename= %s" % filename)
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        # Segurança
        s.starttls()

        s.login(self.fromaddr, self.password)

        # Converte para String
        text = msg.as_string()

        s.sendmail(self.fromaddr, self.toaddr, text)
        print('E-mails enviados')