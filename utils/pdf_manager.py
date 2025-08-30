from fpdf import FPDF
from pandas import DataFrame
from pathlib import Path
class PDFManager(FPDF):
    """Classe responsavel por gerar o relatorio PDF

    Args:
        FPDF (_type_): lib fpdf
    """

    def __init__(self, orientation = "portrait", unit = "mm", format = "A4", font_cache_dir = "DEPRECATED"):
        super().__init__(orientation, unit, format, font_cache_dir)

        self.reports_folder = Path(Path(__file__).parent.parent, "reports")

        if not self.reports_folder.exists():
            self.reports_folder.mkdir()

    def header(self):
        """Cria o headers das paginas do pdf
        """

        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório de Endereços por CEP', 0, 1, 'C')
        self.set_font('Arial', 'I', 8)
        self.ln(5)

    def footer(self):
        """Cria o footers das paginas do pdf
        """

        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def create_table(self, dataframe:DataFrame, col_widths:list = [20, 45, 30, 35, 42, 25, 85]):
        """Cria a tabela de relatorio com dados utilizando um data frame

        Args:
            dataframe (DataFrame): pandas dataframe
            col_widths (list, optional): define a largura das colunas da tabela. Defaults to [20, 45, 30, 35, 42, 25, 85].
        """


        self.set_font('Arial', 'B', 10)
        self.set_fill_color(200, 220, 255) 
        
        header_labels = [col.replace('_', ' ').title() for col in dataframe.columns]

        for i, header in enumerate(header_labels):
            self.cell(col_widths[i], 10, header, 1, 0, 'C', fill=True)
        self.ln()

        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        
        for index, row in dataframe.iterrows():
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, str(item), 1, 0, 'L')
            self.ln()

    def make_report(self, dataframe:DataFrame) -> str:
        """Cria o relatorio em PDF

        Args:
            dataframe (DataFrame): pandas Dataframe

        Returns:
            str: caminho absoluto para o relatorio em PDF
        """

        report_path = f"{self.reports_folder}/relatorio.pdf"

        self.add_page()

        self.set_auto_page_break(auto=True, margin=15)

        self.create_table(dataframe)

        self.output(report_path)

        return report_path