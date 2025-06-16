import win32com.client
from ../lib.py import is_email_valid
def Mail:
    def __init__(self,sender,receiver,subject,body):
        self.__outlook=win32com.client.Dispatch("Outlook.Application")
        if not is_email_valid(sender):
            raise ValueError("Sender email is not valid")
        if not is_email_valid(receiver):
            raise ValueError("Receiver email is not valid")
        self.__sender=sender
        self.__receiver=receiver
        self.__subject=subject
        self.__body=body
        self.__g_attachments=[]
        self.__p_attachments=[]
    def is_sender_valid(self):
        session = self.__outlook.Session
        accounts = session.Accounts

        for account in accounts:
            if account.SmtpAddress.lower() == self.sender:
                return True
        return False
    def add_general_attachment(self,path):
        self.__g_attachments.append(path)
    def add_personal_attachment(self,path):
        self.__p_attachments.append(path)
    def send(self,send=True):
        if not self.is_sender_valid():
            raise ValueError("Sender email is not valid")
        mail = self.__outlook.CreateItem(0)
        mail.To = self.__receiver
        mail.Subject = self.__subject
        mail.Body = self.__body
        for attachment in self.__g_attachments:
            mail.Attachments.Add(attachment)
        for attachment in self.__p_attachments:
            mail.Attachments.Add(attachment)
        if send:
            mail.Send()
        else:
            mail.Display()