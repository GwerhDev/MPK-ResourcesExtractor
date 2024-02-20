import PySimpleGUI as sg

layout_format = [
  [sg.Text("Select file formats to extract:", background_color='#15171E')],
  [
    sg.Checkbox('.jpg', key='-JPG-', background_color='#15171E'), 
    sg.Checkbox('.png', key='-PNG-', background_color='#15171E'),
    sg.Checkbox('.gif', key='-GIF-', background_color='#15171E'), 
    sg.Checkbox('.mp3', key='-MP3-', background_color='#15171E'),
    sg.Checkbox('.mp4', key='-MP4-', background_color='#15171E')
  ],
]