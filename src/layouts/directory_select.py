import PySimpleGUI as sg

layout_dir = [
  [sg.Text("Select output directory for extracted files:", background_color='#15171E')],
  [sg.Input(key="-FOLDER-", size=(42, 1)), sg.FolderBrowse(button_text='Choose', size=(8, 1))],
]