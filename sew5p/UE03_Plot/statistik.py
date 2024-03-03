import argparse
import logging
import os
from collections import Counter
from logging.handlers import RotatingFileHandler
from subprocess import Popen, PIPE
import matplotlib.pyplot as plt
import numpy as np


def get_logger(args: argparse.Namespace) -> logging.Logger:
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
    logger = get_logger(args)
    try:
        git_log = ["git", "-C", args.file, "log", "--pretty=format:%ad", "--date=format-local:%a-%H-%M"]
        process = Popen(git_log, stdout=PIPE, stderr=PIPE, text=True)
        out, err = process.communicate()
        logger.debug("Data Retrived")
        time_window = 0.5
        tage = ["", "mo", "di", "mi", "do", "fr", "sa", "so", ""]
        if err:
            logger.error(err)
        dateng = Counter()
        numberCommits = 0
        for i in out.splitlines():
            tmp = i.split("-")
            dateng[(tmp[0].lower(), (np.floor((int(tmp[1]) + int(tmp[2]) / 60) / time_window) * time_window))] += 1
            numberCommits += 1

        logger.debug("Daten verarbeitet")

        minSize = 100
        sizeinc = 50

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

        plt.xlabel('Time')
        plt.title(f'Luca Sautter: {numberCommits} commits')
        plt.grid(True, which="major", axis="y", linestyle="-", linewidth=2, color='black')
        plt.xlabel('Tag')
        logger.debug("Daten verarbeitet")

        plt.savefig("statistic.png", dpi=72)

        logger.info("Grafik ausgegeben")
    except:
        logger.error("You're in trouble here!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Pfad des Verzeichnises mit .git ordner")
    mutuagroup = parser.add_mutually_exclusive_group()
    mutuagroup.add_argument("-v", "--verbose", action="store_true", help="Log Level verbose")
    mutuagroup.add_argument("-q", "--quiet", action="store_true", help="Log Level quiet")
    args = parser.parse_args()
    main(args)