import PySimpleGUI as sg

def select_file():
  image_path = "src/assets/logo.png"
  layout = [
    [sg.Image(filename=image_path, size=(380, 380))],
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
          
def select_output_directory():
  layout = [
    [sg.Text("Select output directory for extracted files:")],
    [sg.Input(key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Button("OK")]
  ]
  window = sg.Window("Select Directory", layout)

  while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
      folder = "results"
      break
    elif event == "OK":
      folder = values["-FOLDER-"]
      break

  window.close()
  return folder