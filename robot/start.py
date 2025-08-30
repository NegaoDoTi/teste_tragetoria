from utils.driver import Driver
from utils.driver import ChromeWebdriver
from utils.csv_manager import CSVManager
from robot.pages.index_page import IndexPage
from robot.pages.cep_page import CepPage
from traceback import format_exc
import logging

class StartRobot():
    def __init__(self):
        self.driver:ChromeWebdriver
        self.__index_page:IndexPage
        self.__cep_page:CepPage

    def run(self, ceps:list) -> None:
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

        except Exception:
            print(format_exc())