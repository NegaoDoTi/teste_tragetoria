from time import sleep
from traceback import format_exc
from os import system
import pyautogui
import logging

def calculator(ceps:list[dict]) -> None:
    """Script que digita todos os cep na calculadora do Windows 10

    Args:
        ceps (list[dict]): lista de dicionarios contendo os ceps a serem digitados
    """

    try:
        system("calc.exe")
    except Exception:
        print("Nâo foi possivel abrir a calculadora")

        logging.error(f"Não foi possivel abrir a calculadora, {format_exc()}")

        return

    sleep(3)

    for cep in ceps:
        cep = cep["CEP"].replace("-", "")

        try:
            calculator = pyautogui.getWindowsWithTitle('Calculadora')[0]
            calculator.activate()

        except Exception:
            print("A janela da Calculadora não foi encontrada.")

            logging.error(f"A janela da Calculadora não foi encontrada, {format_exc()}")

            return
        
        pyautogui.write(cep, interval=0.5)

        sleep(0.5)

        pyautogui.press("esc")

        sleep(0.5)

    print("Script de calculadora correu com sucesso!")

    return