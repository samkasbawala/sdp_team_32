"""The purpose of this module is to be able to download the datesets that are
needed in order for this project. We will be using the game logs that
available from retrosheet.org. A huge thank you to them for having such an
extensive collection of game logs. All of the data from their website is the
result of countless hours of VOLUNTEER work. We appreciate their efforts and
this project could not have been done without them"""

from tqdm import tqdm
import requests
import os
import zipfile


class DownloadRetroSheetData():
    def __init__(self,
                 years=list(range(2014, 2020)),
                 url="https://www.retrosheet.org/gamelogs/",
                 download_path="./datasets/retro_sheet_gls"):
        self.years = years
        self.url = url
        self.download_path = download_path

    def run(self):
        # Download the zip files and extract them
        self.__download(self.url, self.years, self.download_path)

        # Add the labels on the text files
        self.__makeLabels([os.path.join(self.download_path, f)
                           for f in os.listdir(self.download_path)])

    def __download(self, url, years, download_path):
        """This method downloads the gamelog files from the retrosheet website

        The gamelog files are zipped. We need to extract them to reveal the
        .txt files. The .txt files don't have labels, so we will likely have
        to label ourselves. The default directory is the datasets folder.
        However you can save the files where ever you would like.
        """

        # Make the directory in case it doesn't exist
        if not os.path.exists(download_path):
            os.mkdir(download_path)

        # Delete all existing files in the directory
        current_files = [f for f in os.listdir(download_path)]
        for f in current_files:
            os.remove(os.path.join(download_path, f))

        # Download each gamelog and unzip the file
        # Display progress using tqdm progress bar
        with tqdm(total=len(years), unit="log") as pbar:
            for year in years:
                # Download the file
                pbar.set_description(f"Downloading {year} gamelog")
                r = requests.get(url+f"gl{year}.zip")
                with open(os.path.join(download_path, f"gl{year}.zip"), "wb") as f:
                    f.write(r.content)

                # Unzip the file
                pbar.set_description(f"Unzipping gl{year}.zip")
                with zipfile.ZipFile(os.path.join(download_path,
                                                  f"gl{year}.zip"),
                                     "r") as zip_ref:
                    zip_ref.extractall(download_path)

                # Delete the zipped file
                os.remove(os.path.join(download_path, f"gl{year}.zip"))
                pbar.update()

    def __makeLabels(self, files, labels = [
            "Date",
            "Number of game",
            "Day",
            "Visiting Team",
            "Visiting Team League",
            "Visiting Team Game Number",
            "Home Team",
            "Home Team League",
            "Home Team Game Number",
            "Visiting Team Score",
            "Home Team Score",
            "Length of Game (outs)",
            "Time of Game (Day/Night)",
            "Completion Information",
            "Forfeit Information",
            "Protest Information",
            "Park ID",
            "Attendance",
            "Length of Game (minutes)",
            "Visiting Team Line Score",
            "Home Team Line Score",
            "Visiting Team At-bats",
            "Visiting Team Hits",
            "Visiting Team Doubles",
            "Visiting Team Triples",
            "Visiting Team Homeruns",
            "Visiting Team RBIs",
            "Visiting Team Sacrifice Hits",
            "Visiting Team Sacrifice Flies",
            "Visiting Team Hit-by-pitch",
            "Visiting Team Walks",
            "Visiting Team Intentional Walks",
            "Visiting Team Strikeouts",
            "Visiting Team Stolen Bases",
            "Visiting Team Caught Stealing",
            "Visiting Team Grounded into DP",
            "Visiting Team Awarded First Base due to CI",
            "Visiting Team Left on Base",
            "Visiting Team Pitchers Used",
            "Visiting Team Individual Earned Runs",
            "Visiting Team Earned Runs",
            "Visiting Team Wild Pitches",
            "Visiting Team Balks",
            "Visiting Team Putouts",
            "Visiting Team Assists",
            "Visiting Team Errors",
            "Visiting Team Passed Balls",
            "Visiting Team Double Plays",
            "Visiting Team Triple Plays",
            "Home Team At-bats",
            "Home Team Hits",
            "Home Team Doubles",
            "Home Team Triples",
            "Home Team Homeruns",
            "Home Team RBIs",
            "Home Team Sacrifice Hits",
            "Home Team Sacrifice Flies",
            "Home Team Hit-by-pitch",
            "Home Team Walks",
            "Home Team Intentional Walks",
            "Home Team Strikeouts",
            "Home Team Stolen Bases",
            "Home Team Caught Stealing",
            "Home Team Grounded into DP",
            "Home Team Awarded First Base due to CI",
            "Home Team Left on Base",
            "Home Team Pitchers Used",
            "Home Team Individual Earned Runs",
            "Home Team Earned Runs",
            "Home Team Wild Pitches",
            "Home Team Balks",
            "Home Team Putouts",
            "Home Team Assists",
            "Home Team Errors",
            "Home Team Passed Balls",
            "Home Team Double Plays",
            "Home Team Triple Plays",
            "Home Plate Umpire ID",
            "Home Plate Umpire Name",
            "1B Umpire ID",
            "1B Umpire Name",
            "2B Umpire ID",
            "2B Umpire Name",
            "3B Umpire ID",
            "3B Umpire Name",
            "LF Umpire ID",
            "LF Umpire Name",
            "RF Umpire ID",
            "RF Umpire Name",
            "Visiting Team Manager ID",
            "Visiting Team Manager Name",
            "Home Team Manager ID",
            "Home Team Manager Name",
            "Winning Pitcher ID",
            "Winning Pitcher Name",
            "Losing Pitcher ID",
            "Losing Pitcher Name",
            "Saving Pitcher ID",
            "Saving Pitcher Name",
            "Game Winning RBI Batter ID",
            "Game WInning RBI Batter Name",
            "Visiting Team Starting Pitcher ID",
            "Visiting Team Starting Pitcher Name",
            "Home Team Starting Pitcher ID",
            "Home Team Starting Pitcher Name",
            "Visiting Team Player 1 ID",
            "Visiting Team Player 1 Name",
            "Visiting Team Player 1 Defensive Position",
            "Visiting Team Player 2 ID",
            "Visiting Team Player 2 Name",
            "Visiting Team Player 2 Defensive Position",
            "Visiting Team Player 3 ID",
            "Visiting Team Player 3 Name",
            "Visiting Team Player 3 Defensive Position",
            "Visiting Team Player 4 ID",
            "Visiting Team Player 4 Name",
            "Visiting Team Player 4 Defensive Position",
            "Visiting Team Player 5 ID",
            "Visiting Team Player 5 Name",
            "Visiting Team Player 5 Defensive Position",
            "Visiting Team Player 6 ID",
            "Visiting Team Player 6 Name",
            "Visiting Team Player 6 Defensive Position",
            "Visiting Team Player 7 ID",
            "Visiting Team Player 7 Name",
            "Visiting Team Player 7 Defensive Position",
            "Visiting Team Player 8 ID",
            "Visiting Team Player 8 Name",
            "Visiting Team Player 8 Defensive Position",
            "Visiting Team Player 9 ID",
            "Visiting Team Player 9 Name",
            "Visiting Team Player 9 Defensive Position",
            "Home Team Player 1 ID",
            "Home Team Player 1 Name",
            "Home Team Player 1 Defensive Position",
            "Home Team Player 2 ID",
            "Home Team Player 2 Name",
            "Home Team Player 2 Defensive Position",
            "Home Team Player 3 ID",
            "Home Team Player 3 Name",
            "Home Team Player 3 Defensive Position",
            "Home Team Player 4 ID",
            "Home Team Player 4 Name",
            "Home Team Player 4 Defensive Position",
            "Home Team Player 5 ID",
            "Home Team Player 5 Name",
            "Home Team Player 5 Defensive Position",
            "Home Team Player 6 ID",
            "Home Team Player 6 Name",
            "Home Team Player 6 Defensive Position",
            "Home Team Player 7 ID",
            "Home Team Player 7 Name",
            "Home Team Player 7 Defensive Position",
            "Home Team Player 8 ID",
            "Home Team Player 8 Name",
            "Home Team Player 8 Defensive Position",
            "Home Team Player 9 ID",
            "Home Team Player 9 Name",
            "Home Team Player 9 Defensive Position",
            "Miscellaneous",
            "Acquisition Information"
        ]):

        # Prepend the labels array to all of the files
        for file in files:
            self.__prependLines(','.join(labels), file)

    def __prependLines(self, line, file):
        """Insert line at the beginning of the file"""

        # Create a dummy file
        dummy_file = file + ".bak"

        # Open original file as read only and dummy as write
        with open(file, 'r') as readfile, open(dummy_file, 'a') as writefile:

            # Write the line at the beginning of the dummy file
            writefile.write(line + '\n')

            # Copy the contents from the original file to the dummy
            for row in readfile:
                writefile.write(row)

        # Replace the original file with the dummy file
        os.remove(file)
        os.rename(dummy_file, file)
