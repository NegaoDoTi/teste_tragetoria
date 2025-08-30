from csv import DictReader
from pathlib import Path
from csv import DictWriter
from pathlib import Path

class CSVManager():
    def __init__(self):
        self.reports_folder = Path(Path(__file__).parent.parent, "reports")

        if not self.reports_folder.exists():
            self.reports_folder.mkdir()

    def make_report(self, cep_datas:list[dict]) -> str:
            csv_path = f"{self.reports_folder}/relatorio.csv"

            with open(csv_path, "w+") as csv_file:

                header = cep_datas[0].keys()

                writer = DictWriter(csv_file, fieldnames=header, delimiter=";")

                writer.writeheader()

                writer.writerows(cep_datas)

                csv_file.close()

            return csv_path

    def read_csv(self, csv_path:str) -> list:

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