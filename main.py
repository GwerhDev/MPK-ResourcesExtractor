import PySimpleGUI as sg
import glob
import os
import subprocess
from src.functions.unpack import *
from src.functions.file import *

def main():
    mpkinfo_file = select_file()
    if mpkinfo_file:
        basename = ""
        resource_files = []

        if(mpkinfo_file.lower().endswith(".mpkinfo")):
            # fix mismatching file names for Resource*.mpk
            if(mpkinfo_file.lower().startswith("resource")):
                basename = "Resources"
            else:
                basename = mpkinfo_file.split(".")[0]

            mpk_files = glob.glob(basename + "*.mpk")

            resource_files.append(basename + ".mpk")

            unpack_archive(mpkinfo_file, resource_files)  # Extract directly after file selection

            sg.popup("Successful extraction", title="Success")
            subprocess.Popen(['explorer', os.path.abspath("results")])  # Opens "results" folder once finished
        else:
            sg.popup_error("Please select a valid MPKINFO file.")

if __name__ == "__main__":
    main()
