from requests import get
from traceback import format_exc

class ViaCepGateway():

    def search_cep(self, cep_data:dict) -> dict[bool, str, str, dict]:
        try:
            error_message = f"O Cep: {cep_data['cep']} não foi entrado em nenhuma das bases de dados Busca CEP/Via CEP"

            response = get(url=f"https://viacep.com.br/ws/{cep_data['cep']}/json/", verify=False)

            if response.status_code != 200:
                cep_data["status"] = "CEP não encontrado nas duas bases de dados Busca CEP e Via CEP"
                
                return {
                    "error" : True,
                    "type" :error_message,
                    "exception" : error_message,
                    "data" : cep_data
                }
            
            data = response.json()

            if "erro" in data:
                cep_data["status"] = "CEP não encontrado nas duas bases de dados Busca CEP e Via CEP"
                
                return {
                    "error" : True,
                    "type" :error_message,
                    "exception" : error_message,
                    "data" : cep_data
                }
            
            cep_data["lougadouro"] = data["logradouro"]
            cep_data["bairro"] = data["bairro"]
            cep_data["cidade"] = data["localidade"]
            cep_data["estado"] = data["estado"]
            cep_data["regiao"] = data["regiao"]
            cep_data["status"] = "SUCESSO, extraído de Via CEP"


            return {
                "error" : False,
                "type" :"",
                "exception" : "",
                "data" : cep_data
            }        

        except Exception:
            cep_data["status"] = "CEP não encontrado na Busca CEP e na Via CEP"
            
            return {
                "error" : True,
                "type" :error_message,
                "exception" : f"{format_exc()}",
                "data" : cep_data
            }