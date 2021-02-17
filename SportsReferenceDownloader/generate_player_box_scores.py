import os
import shutil
import pandas as pd

from sportsreference.mlb.roster import Player


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


def GeneratePlayerBoxScores(team):
    """Function that takes a Team object and returns a dataframe object
    containing the boxscore of each player that played in a game"""

    team_dfs = []
    for game in team.schedule:

        # Home team players
        for player in game.boxscore.home_players:
            df = player.dataframe
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'player_id'}, inplace=True)
            df['uri'] = game.boxscore_index
            df['date'] = game.datetime
            team_dfs.append(df)

        # Away team players
        for player in game.boxscore.away_players:
            df = player.dataframe
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'player_id'}, inplace=True)
            df['uri'] = game.boxscore_index
            df['date'] = game.datetime
            team_dfs.append(df)

    # Return a concatenated dataframe object
    return pd.concat(team_dfs, ignore_index=True)


def GeneratePlayerNames(player_id):
    """Function that takes in a player ids and returns the name as a tuple"""

    return (player_id, Player(player_id).name)


if __name__ == '__main__':
    pass
