import PySimpleGUI as sg
import glob
import os
import subprocess
from functions.unpack import *

def select_file():
    layout = [
        [sg.Text("Select MPKINFO file:")],
        [sg.Input(key="-FILE-"), sg.FileBrowse()],
        [sg.Button("Extract"), sg.Button("Cancel")]
    ]

    window = sg.Window("MPK Extractor", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            window.close()
            return None
        elif event == "Extract":
            return values["-FILE-"]

if __name__ == "__main__":
    mpkinfo_file = select_file()
    if mpkinfo_file:
        basename = ""
        resource_files = []
        resource_info = mpkinfo_file

        if(mpkinfo_file.lower().endswith(".mpkinfo")):
            # fix mismatching file names for Resource*.mpk
            if(mpkinfo_file.lower().startswith("resource")):
                basename = "Resources"
            else:
                basename = mpkinfo_file.split(".")[0]

            mpk_files = glob.glob(basename + "*.mpk")

            resource_files.append(basename + ".mpk")

            unpack_archive(mpkinfo_file, resource_files)  # Extract directly after file selection

            sg.popup("Extracción exitosa", title="Success")
            subprocess.Popen(['explorer', os.path.abspath("results")])  # Opens "results" folder once finished
        else:
            sg.popup_error("Please select a valid MPKINFO file.")
