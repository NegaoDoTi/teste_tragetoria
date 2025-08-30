from config.env import EMAIL, EMAIL_PASSWORD
from email.message import EmailMessage
from smtplib import SMTP
from traceback import format_exc
import logging

class EmailSender():
    """Classe responsavel por montar o email e envia-lo
    """

    def __init__(self):
        self.__email = EMAIL
        self.__email_password = EMAIL_PASSWORD
    
    def start_connection(self) -> None:
        """Conecta e faz login no servidor SMTP do Gmail
        """

        self.__server = SMTP("smtp.gmail.com", 587)

        self.__server.starttls()

        self.__server.login(self.__email, self.__email_password)

        return

    def close_connection(self) -> None:
        """Desconecata do servidor SMTP
        """
        self.__server.close()

        return

    def send_email(self, cep_data:dict, email_recipient:str) -> bool:
        """Monta corpo do email e o envia para o destinatario
        """
        
        try:
            subject = f"Dados cep: {cep_data['cep']}"

            body_title = f"Segue os dados referente ao cep: {cep_data['cep']}"
            
            if "SUCESSO" not in cep_data["status"]:
                body_title = f"Não foi possivel buscar dados do cep: {cep_data['cep']}"

            body = f"""
            Olá

            {body_title}

            Lougadouro: {cep_data['lougadouro']}
            Bairro: {cep_data['bairro']}
            Cidade: {cep_data['cidade']}
            Estado: {cep_data['estado']}
            Região: {cep_data['regiao']}
            STATUS: {cep_data['status']}

            Atensiosamente, 

            Robo Trajetoria.
            
            """

            message = EmailMessage()
            message.set_content(body)
            message["Subject"] = subject
            message["From"] = self.__email
            message["to"] = email_recipient

            self.__server.send_message(message)

            return True
        
        except Exception:
            logging.error(f"Não foi possivel enviar email para: {email_recipient}, {format_exc()}")

            return False
    
