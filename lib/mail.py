import win32com.client
import os
from ../lib.py import is_email_valid,archivo_existe
class Mail:
    def __init__(self,sender,receiver,subject):
        self.__outlook=win32com.client.Dispatch("Outlook.Application")
        if not is_email_valid(sender):
            raise ValueError("Sender email is not valid")
        if not is_email_valid(receiver):
            raise ValueError("Receiver email is not valid")
        self.__sender=sender
        self.__receiver=receiver
        self.__other=[]
        self.__cc=[]
        self.__subject=subject
        self.__body=""
        self.__g_attachments=[]
        self.__p_attachments=[]
    def is_sender_valid(self):
        """
        Verifica si el remitente está registrado en la sesión actual de Outlook.

        Returns:
            bool: True si el email del remitente está configurado en Outlook, False en caso contrario.
        """
        session = self.__outlook.Session
        accounts = session.Accounts

        for account in accounts:
            if account.SmtpAddress.lower() == self.sender:
                return True
        return False
    def add_other(self,email):
        """
        Añade un correo adicional a la lista de destinatarios.

        Args:
            email (str): Email del destinatario adicional.
        """
        if not is_email_valid(email):
            raise ValueError("Email is not valid")
        self.__other.append(email)
    def add_cc(self,email):
        if not is_email_valid(email):
            raise ValueError("Email is not valid")
        self.__cc.append(email)
    def add_general_attachment(self,path):
        """
        Añade un archivo a la lista de adjuntos generales.

        Args:
            path (str): Ruta absoluta o relativa del archivo que se desea adjuntar.
        """
        if not archivo_existe(path):
            raise ValueError("File does not exist")
        self.__g_attachments.append(path)
    def add_personal_attachment(self,path):
        """
        Añade un archivo a la lista de adjuntos personales.

        Args:
            path (str): Ruta absoluta o relativa del archivo que se desea adjuntar.
        """
        if not archivo_existe(path):
            raise ValueError("File does not exist")
        self.__p_attachments.append(path)
    def set_receiver(self,mail):
        mail.To = f"{self.__receiver}; {';'.join(self.__other)}"
    def set_cc(self,mail):
        mail.Cc = f"{';'.join(self.__cc)}"
    def set_body(self,mail,string):
        mail.HTMLBody = f"<body>{string}</body>"
    def send(self,send=True):
          """
        Crea el correo, agrega los adjuntos y lo envía o muestra según el parámetro.

        Args:
            send (bool, optional): Si es True, el correo se envía inmediatamente.
                                Si es False, se abre la ventana de composición para revisión.
                                Por defecto es True.

        Raises:
            ValueError: Si el email del remitente no está configurado en Outlook.
        """
        if not self.is_sender_valid():
            raise ValueError("Sender email is not valid")
        mail = self.__outlook.CreateItem(0)
        self.set_receiver(mail)
        if len(self.__cc)>0:
            self.set_cc(mail)
        mail.Subject = self.__subject
        self.set_body(mail,self.__body)
        for attachment in self.__g_attachments:
            mail.Attachments.Add(attachment)
        for attachment in self.__p_attachments:
            mail.Attachments.Add(attachment)
        if send:
            mail.Send()
        else:
            mail.Display()