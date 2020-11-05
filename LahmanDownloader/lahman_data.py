import requests
import os
import zipfile
import shutil


class DownloadLahmanData():
    """Class to download data from Sean Lahman's website, specifically data up
    to and including 2019. The url might change once the 2020 season data is
    released."""

    def __init__(self,
                 url=("https://github.com/chadwickbureau/"
                      "baseballdatabank/archive/master.zip"),
                 download_path="./datasets/lahman"):
        self.url = url
        self.download_path = download_path

    def run(self):
        """Public method to download the Lahman datasets"""

        self.__download(self.url, self.download_path)

    def __download(self, url, download_path):
        """This method downloads the data from the provided url

        The data from Lahman's website is zipped. We need to extract them to
        reveal the .csv files.
        """
        # Make the directory in case it doesn't exist
        if not os.path.exists(download_path):
            os.mkdir(download_path)

        # Delete all existing files in the directory
        self.__clean_path(download_path)

        # Download the data
        r = requests.get(url)

        # Write the file
        with open(os.path.join(download_path, "lahman.zip"), "wb") as f:
            f.write(r.content)

        # Unzip the file
        with zipfile.ZipFile(os.path.join(download_path,
                                          "lahman.zip"),
                             "r") as zip_ref:
            zip_ref.extractall(download_path)

        # Delete the zipped folder
        os.remove(os.path.join(download_path, "lahman.zip"))

        # Get subdir folder, it's the only folder in download_path
        sub_dir = os.path.join(download_path, os.listdir(download_path)[0])

        # Move the actual csvs to the download path
        for file in os.listdir(os.path.join(sub_dir, "core")):
            source = os.path.join(sub_dir, "core", file)
            destination = os.path.join(download_path, file)
            shutil.move(source, destination)

        # Delete the subdir
        shutil.rmtree(sub_dir)

    def __clean_path(self, path):
        """Deletes all the files in the folder path that is inputted"""

        # Delete all existing files in the directory
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
