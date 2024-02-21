import PySimpleGUI as sg
import glob
import os
import subprocess
from src.functions.file import *
from src.functions.unpack import *
from src.layouts.logo import layout_logo
from src.layouts.buttons import layout_buttons
from src.layouts.file_select import layout_file
from src.layouts.format_select import layout_format
from src.layouts.directory_select import layout_dir

def interface():
  window = sg.Window(
    "MPK Resources Extractor | Gwerh", [
      layout_logo,
      layout_dir,
      layout_file,
      layout_format,
      layout_buttons,
    ],
    resizable=False,
    no_titlebar=False, 
    grab_anywhere=True,
    background_color='#15171E',
    icon='../src/assets/logo.ico',
  )
  
  mpkinfo_file = select_file(window)

  if mpkinfo_file:
    basename = ""
    resource_files = []

    if(mpkinfo_file["file"].lower().endswith(".mpkinfo")):
      # fix mismatching file names for Resource*.mpk
      if(mpkinfo_file["file"].lower().startswith("resource")):
        basename = "Resources"
      else:
        basename = mpkinfo_file["file"].split(".")[0]

      mpk_files = glob.glob(basename + "*.mpk")

      resource_files.append(basename + ".mpk")
      
      if mpkinfo_file["formats"]:
        unpack_archive(mpkinfo_file["file"], mpkinfo_file["folder"], resource_files, mpkinfo_file["formats"])
      else:
        unpack_archive(mpkinfo_file["file"], mpkinfo_file["folder"], resource_files)

      sg.popup("Successful extraction", title="Success", background_color="#15171E", button_color='#0074e0', icon='../src/assets/logo.ico')

      # Opens "results" folder once finished
      subprocess.Popen(['explorer', os.path.abspath(mpkinfo_file["folder"] + "/MPL Resources Extractor")])
    else:
      sg.popup_error("Please select a valid MPKINFO file.", background_color="#15171E", button_color='#0074e0', icon='../src/assets/logo.ico')