import PySimpleGUI as sg
from resources.utils.lists import file_formats

layout_format = [
  [sg.Text("Select file formats to extract:", background_color='#15171E')],
]

for category in file_formats:
  layout_format.append([sg.Text(category["category"], background_color='#15171E')])
  checkbox_row = []
  for format in category["formats"]:
    checkbox_row.append(sg.Checkbox(format, key=format.replace('.', '-') + '-', background_color='#15171E'))
    if len(checkbox_row) == 5:
      layout_format.append(checkbox_row)
      checkbox_row = []
      
  if checkbox_row:
    layout_format.append(checkbox_row)
