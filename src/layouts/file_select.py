import PySimpleGUI as sg

layout_file = [
  [sg.Text("Select MPKINFO file:", background_color='#15171E')],
  [sg.Input(key="-FILE-"), sg.FileBrowse()],
]