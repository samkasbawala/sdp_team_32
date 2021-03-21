from sportsreference.mlb.schedule import Schedule
from sportsreference.mlb.teams import Teams
from multiprocessing import Pool
from tqdm import tqdm

import pandas as pd
import numpy as np
import os
import shutil


SR_BOXSCORES_PATH = './datasets/sports_reference_boxes'


def clean_dir(path):
    """Makes a clean directory, removes all files and folders in the
    specified path"""

    if not os.path.exists(path):
        os.mkdir(path)

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def getBoxscores(year_start, year_end=None, save_dir=SR_BOXSCORES_PATH):
    if year_end is None:
        year_end = year_start

    clean_dir(save_dir)

    for year in range(year_start, year_end+1):
        print(f'Getting data for {year} season. This may take a while...')

        year_dir = os.path.join(save_dir, str(year))
        clean_dir(year_dir)

        with Pool() as p:
            iterable = [(team, year, year_dir) for team in Teams(year)]
            results = list(tqdm(p.imap(_getDataframe, iterable),
                                total=len(iterable)))


def _getDataframe(tup):
    team, year, year_dir = tup
    abbr = team.abbreviation
    save_path = os.path.join(year_dir, f'{abbr}_{year}')
    dataframe = Schedule(abbr, year).dataframe_extended
    dataframe.to_csv(save_path)


if __name__ == '__main__':
    pass
