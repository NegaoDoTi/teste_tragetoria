from utils.driver import Driver
from utils.driver import ChromeWebdriver
from utils.csv_manager import CSVManager
from utils.pdf_manager import PDFManager
from robot.pages.index_page import IndexPage
from robot.pages.cep_page import CepPage
from utils.email_sender import EmailSender
from scripts.calculator_script import calculator
from traceback import format_exc
from pandas import DataFrame
import logging

class StartRobot():
    """Classe responsavel por orquestrar todas as partes da Automação/Robô
    """

    def __init__(self):
        self.driver:ChromeWebdriver
        self.__index_page:IndexPage
        self.__cep_page:CepPage
        self.__email_sender = EmailSender()

    def run(self, ceps:list[dict]) -> None:
        """Função que a ordem logica de quais parte do robô deve rodar primeiro

        Args:
            ceps (list): list de dicionarios contendo todos os cep a serem buscados
        """

        try:
            self.driver = Driver().get_chrome_driver()
            
            if isinstance(self.driver, dict):
                logging.critical(f'{self.driver["type"]} {self.driver["exception"]}')
                return
            
            self.__index_page = IndexPage(self.driver)
            self.__cep_page = CepPage(self.driver)

            index_result = self.__index_page.open()

            if index_result["error"] == True:
                logging.error(f'{index_result["type"]}, {index_result["exception"]}')
                return
            
            cep_datas = []

            for cep in ceps:

                search_cep = self.__cep_page.search_cep(cep["CEP"])
                if search_cep["error"] == False:
                    cep_datas.append(search_cep["data"])

                else:
                    cep_datas.append(search_cep["data"])

                    logging.error(f"{search_cep["type"]}, {search_cep["exception"]}")

            report = CSVManager().make_report(cep_datas)

            print(f"Relatorio gerado com sucesso: {report}")

            email_recipient = "example@email.com"

            self.__email_sender.start_connection()

            for cep_data in cep_datas:

                email = self.__email_sender.send_email(cep_data, email_recipient)

                if email == False:
                    print(f"Não foi possivel enviar email para {email_recipient}")

            self.__email_sender.close_connection()

            print("Todos os email enviado com sucesso!")

            pdf_manager = PDFManager("L", "mm", "A4")

            result = pdf_manager.make_report(DataFrame(cep_datas))

            print(f"Relatorio em PDF criado com sucesso e salvo em: {result}")

            try:
                self.driver.close()
                self.driver.quit()
            except:
                pass

            calculator(ceps)

            return

        except Exception:
            try:
                self.driver.close()
                self.driver.quit()
            except:
                pass

            logging.critical(f"Erro inesperado ocorreu: {format_exc()}")

            return