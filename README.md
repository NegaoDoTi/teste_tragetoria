## Teste Tecnico Desenvolvedor Python RPA Pleno Trajetoria

## Descrição
O teste consiste em fazer a leitura de um arquivo CSV com uma coluna contendo CEPS,
após fazer a leitura deve ser feita a extração de dados de cada CEP se houver no site: [Busca CEP](https://buscacep.com.br/).

Feita a extração de dados te todos os CEPS, deve ser gerado um relatorio em csv e outro em pdf,
também deve ser enviado um email por CEP contendo uma mensagem personalizada e as informações do CEP. 

Concluída todas essas operações deve se abrir a calculadora do Windows e digitar CEP por CEP.

## Como instalar
1. Instale o [Python 3](https://python.org.br/instalacao-windows/)
2. Instale o [GIT](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git)
3. Clone o repositorio com o comando: `git clone https://github.com/NegaoDoTi/teste_trajetoria`
4. Copie o arquivo **.env.example** para **.env** e digite suas credencias de login do Gmail no **.env**
5. Execute o comando: `pip install -r requirements.txt`
6. FIM

## Como executar:
1. Execute o comando: `python run.py`

## Tecnologias Utilizadas
    Python 3.13
    Pandas
    Fpdf
    Selenium
    Pyautogui

## Relatorios

Os relatorios se encontram na pasta **reports**

## Possiveis melhorias

    1. Integração com RabbitMQ para fazer a extração dos CEPs de forma assincrona
    2. Integração com banco de dados para salvar os dados de cada CEP
    3. Troca do Selenium por bibliotecas BeautifulSoup + httpx e tornar codigo todo async para aumentar performance, tornar concorrente e utilizar menos recursos da máquina.
    4. Utilização de Pydantic para fazer validação dos dados dos CEPs em tempo real com schemas.