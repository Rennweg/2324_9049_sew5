import argparse
import logging
import os
from collections import Counter
from logging.handlers import RotatingFileHandler
from subprocess import Popen, PIPE
import matplotlib.pyplot as plt
import numpy as np

def get_logger(args: argparse.Namespace) -> logging.Logger:
    """
    Standard Methode welche Loggin configuriert
    :param args:
    :return:
    """
    logger = logging.getLogger('logger')
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    elif args.quiet:
        logger.setLevel(logging.WARNING)
    else:
        logger.setLevel(logging.INFO)
    if not os.path.exists("log"):
        os.mkdir("log")
    file_handler = RotatingFileHandler("./log/statistic.log", maxBytes=10000, backupCount=5)
    file_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s %(message)s'))
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter('%(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.info("Logging wurde aktiviert mit dem Level: " + str(logger.level))
    return logger



def main(args: argparse.Namespace) -> None:
    """
    Main methode welche in dem mitgegebnen verzeichnis den git befehl ausführt und daraus die Grafik erstellt.
    :param args:
    :return:
    """
    logger = get_logger(args)
    tage = ['', 'mo', 'di', 'mi', 'do', 'fr', 'sa', 'so', '']
    time_window = 0.5 #in welchem Interval Commits gegrouped werden (in stunden)
    numberCommits = 0 # Startcounter commit
    minSize = 100 # Startsize von dem Punkt bei Commits in grafik
    sizeinc = 50 # Incremet der Size des Punktes pro Commit
    try:
        git_log = ["git", "-C", args.file, "log", "--pretty=format:%ad", "--date=format-local:%a-%H-%M"]
        process = Popen(git_log, stdout=PIPE, stderr=PIPE, text=True)
        out, error = process.communicate()
        logger.debug("Data Retrived")
        #Zum debugen sehr hilfreich, wenn man die genaue Fehlermeldunng von Popen hat
        if error:
            logger.error(error)
        dateng = Counter()
        outLines = out.splitlines()
        for line in outLines:
            d, h, m = line.split("-")
            dateng[(d.lower(), (np.floor((int(h) + int(m) / 60) / time_window) * time_window))] += 1
            numberCommits += 1

        logger.debug("Daten verarbeitet")

        data = {"x": [], "y": [], "size": []}
        for day, time in dateng:
            data["x"].append(time)
            data["y"].append(tage.index(day))
            data["size"].append(minSize + sizeinc * dateng[(day, time)])
        plt.figure(figsize=(10, 8))

        plt.ylabel('Wochentage')
        plt.scatter(data['x'], data['y'], s=data['size'], alpha=1)
        plt.yticks(range(len(tage)), labels=tage)
        plt.xticks(range(0, 25, 4))

        plt.title(f'Luca Sautter: {numberCommits} commits')
        plt.grid(True, which="major", axis="y", linestyle="-", linewidth=2, color='black')
        plt.xlabel('Uhrzeit')
        logger.debug("Daten verarbeitet")

        plt.savefig("statistic.png", dpi=72)

        logger.info("Grafik ausgegeben")
    except:
        logger.error("You're in trouble here!")


if __name__ == "__main__":
    """
    Methodenaufruf der Main Methode und Args Parser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Pfad des Verzeichnises mit .git ordner")
    mutuagroup = parser.add_mutually_exclusive_group()
    mutuagroup.add_argument("-v", "--verbose", action="store_true", help="Log Level verbose")
    mutuagroup.add_argument("-q", "--quiet", action="store_true", help="Log Level quiet")
    args = parser.parse_args()
    main(args)