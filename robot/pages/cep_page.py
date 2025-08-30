from utils.driver import ChromeWebdriver
from utils.waits import Waits
from traceback import format_exc
from gateways.via_cep import ViaCepGateway
from time import sleep

class CepPage():
    def __init__(self, driver:ChromeWebdriver):
        self.__driver:ChromeWebdriver = driver
        self.__waits:Waits = Waits(self.__driver)
        self.via_cep_gateway = ViaCepGateway()

    def search_cep(self, cep:str) -> dict[bool, str, str, dict]:
        try:

            cep = cep.replace("-", "")

            self.__driver.get(f"https://buscacep.com.br/cep/{cep}")

            cep_data = {
                "cep" : cep,
                "lougadouro" : "",
                "bairro" : "",
                "cidade" : "",
                "estado" : "",
                "regiao" : "",
                "status" : ""
            }

            
            try:
                undefined = self.__waits.wait_visibility(
                    {
                        "css_selector" : 'div[class="card-header bg-danger text-white"] h4'
                    },
                    time=3
                )

                if undefined.text.strip() == "CEP não encontrado":
                    
                    response = self.via_cep_gateway.search_cep(cep_data)

                    if response["error"] == True:
                        return response

            except:
                pass

            infos = self.__waits.wait_visibility_all(
                {
                    "css_selector" : 'div[class="col-md-6 mb-3"] div[class="info-item"] label'
                },
                time=5
            )

            datas = self.__waits.wait_visibility_all(
                {
                    "css_selector" : 'p[class="form-control-plaintext fs-5"]'
                },
                time=5
            )

            for i, info in enumerate(infos):

                if "LOGRADOURO" in info.text.strip().upper():
                    cep_data["lougadouro"] = datas[i].text.strip()
                    continue

                if "BAIRRO" in info.text.strip().upper():
                    cep_data["bairro"] = datas[i].text.strip()
                    continue

                if "CIDADE" in info.text.strip().upper():
                    cep_data["cidade"] = datas[i].text.strip()
                    continue

                if "ESTADO" in info.text.strip().upper():
                    cep_data["estado"] = datas[i].text.strip()
                    continue
                
                if "REGIÃO" in info.text.strip().upper():
                    cep_data["regiao"] = datas[i].text.strip()
                    continue

            cep_data["status"] = "SUCESSO, extraído de Busca CEP"

            return {
                "error" : False,
                "type" : "",
                "exception" : "",
                "data" : cep_data
            }

        except Exception:
            cep_data["status"] = "Erro inesperado pegar dados do cep"

            return {
                "error" : True,
                "type" : f"Erro inesperado pegar dados do cep: {cep}",
                "exception" : f"{format_exc()}",
                "data" : cep_data
            }