import PySimpleGUI as sg

def select_file():
  image_path = "src/assets/logo.png"
  layout_logo = [
    [sg.Image(filename=image_path, size=(380, 380))],
  ]

  layout_dir = [
    [sg.Text("Select output directory for extracted files:")],
    [sg.Input(key="-FOLDER-"), sg.FolderBrowse(button_text='Choose')],
  ]

  layout_file = [
    [sg.Text("Select MPKINFO file:")],
    [sg.Input(key="-FILE-"), sg.FileBrowse()],
    [sg.Button("Extract"), sg.Button("Close")]
  ]

  window = sg.Window("MPK Extractor", [layout_logo, layout_dir, layout_file])

  while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Close":
      window.close()
      return None
    elif event == "Extract":
      folder = values["-FOLDER-"]
      file = values["-FILE-"]
      return {"folder": folder, "file": file}
