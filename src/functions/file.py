import PySimpleGUI as sg

def select_file(window):
  while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Close":
      window.close()
      return None
    elif event == "Extract":
      folder = values["-FOLDER-"]
      file = values["-FILE-"]
      formats = [
        ".jpg" if values['-JPG-'] else "",
        ".png" if values['-PNG-'] else "",
        ".gif" if values['-GIF-'] else "",
        ".mp3" if values['-MP3-'] else "",
        ".mp4" if values['-MP4-'] else "",
      ]
      
      # Filter empty format
      formats = [format for format in formats if format]
      return {"folder": folder, "file": file, "formats": formats}
