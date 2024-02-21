import PySimpleGUI as sg
from src.functions.format import select_format


def select_file(window):
  while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Close":
      window.close()
      return None
    elif event == "Extract":
      folder = values["-FOLDER-"]
      file = values["-FILE-"]
      formats = select_format(values)
      
      # Filter empty format
      formats = [format for format in formats if format]
      return {"folder": folder, "file": file, "formats": formats}
