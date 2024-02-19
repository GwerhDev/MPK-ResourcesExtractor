import PySimpleGUI as sg

def show_progress_bar():
    layout = [[sg.ProgressBar(max_value=100, orientation='h', size=(20, 20))]]
    window = sg.Window('Processing', layout, finalize=True, disable_close=True)
    progress_bar = window[0]
    return window, progress_bar