from utils.driver import ChromeWebdriver
from utils.waits import Waits
from traceback import format_exc
from time import sleep

class IndexPage():
    """Classe responsavel pela pagina de Index do site Busca CEP
    """

    def __init__(self, driver:ChromeWebdriver):
        self.__driver:ChromeWebdriver = driver
        self.waits:Waits = Waits(self.__driver)

    def open(self) -> dict[bool, str, str]:
        """Função de carrega o site Busca CEP pela primeira vez, na pagina index

        Returns:


            dict[bool, str, str]: informa se ocorreu um erro na execução
        """

        try:
            self.__driver.get(url="https://buscacep.com.br/")

            sleep(3)

            return {
                "error" : False, 
                "type" : "", 
                "exception" : ""
            }

        except Exception:
            return {
                "error" : True, 
                "type" : "Erro ao carregar web site tente novamente mais tarde", 
                "exception" : f"{format_exc()}"
            }
        