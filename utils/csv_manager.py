from csv import DictReader
from pathlib import Path
from csv import DictWriter
from pathlib import Path

class CSVManager():
    """Class responsavel por fazer o manegamento de arquivos csv, lendo e gerando relatorio
    """

    def __init__(self):
        self.reports_folder = Path(Path(__file__).parent.parent, "reports")

        if not self.reports_folder.exists():
            self.reports_folder.mkdir()

    def make_report(self, cep_datas:list[dict]) -> str:
        """Cria o relatorio em CSV

        Args:
            cep_datas (list[dict]): lista contendo os dados de todos os ceps

        Returns:

        
            str: caminho absoluto aonde o relatorio foi gerado
        """

        csv_path = f"{self.reports_folder}/relatorio.csv"

        with open(csv_path, "w+") as csv_file:

            header = cep_datas[0].keys()

            writer = DictWriter(csv_file, fieldnames=header, delimiter=";")

            writer.writeheader()

            writer.writerows(cep_datas)

            csv_file.close()

        return csv_path

    def read_csv(self, csv_path:str) -> list:
        """Efetua a leitura do arquivo csv aonde contem o ceps crus

        Args:
            csv_path (str): caminho absoluto do arquivo csv contendo os ceps

        Raises:
            Exception: Levanta um erro caso o arquivo não exista
            Exception: Levanta um erro caso o arquivo não seja csv

        Returns:


            list: retorna um lista de dicionarios contendo os cep lidos do csv
        """

        csv_file = Path(csv_path)

        if not csv_file.exists():
            raise Exception(f"O arquivo: {csv_path} não existe!")
        
        if "csv" != csv_file.name.split(".")[-1]:
            raise Exception(f"O tipo do arquivo: {csv_file} não é csv")
        
        ceps = []

        with open(f"{csv_file}", "r+") as file:
            for row in DictReader(file):
                ceps.append(row)

        return ceps