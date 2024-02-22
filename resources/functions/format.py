import PySimpleGUI as sg

def select_format(values):
  selected_formats = []
  for key, value in values.items():
    if value and key.startswith("-") and key not in ["-FILE-", "-FOLDER-"]:
      selected_formats.append('.' + key[1:].replace('-', '.').rstrip('.'))
  return selected_formats
