from robot.start import StartRobot
from utils.csv_manager import CSVManager
from traceback import format_exc
import logging

logging.basicConfig(filename="robot.log", level=logging.INFO, format="%(asctime)s [%(name)s] [%(levelname)s] - %(message)s",)

def run() -> None:
    try:
        ceps = CSVManager().read_csv("./ceps_lista_30.csv")
    except Exception:
        logging.critical(f"{format_exc()}")
        return

    robot = StartRobot()

    robot.run(ceps=ceps)

    return

if __name__ == "__main__":
    run()