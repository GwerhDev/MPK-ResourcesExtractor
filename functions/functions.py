import os
import PySimpleGUI as sg
from PySimpleGUI import ProgressBar

def show_progress_bar():
    layout = [[sg.ProgressBar(max_value=100, orientation='h', size=(20, 20))]]
    window = sg.Window('Processing', layout, finalize=True, disable_close=True)
    progress_bar = window[0]  # Obtenemos la barra de progreso del layout
    return window, progress_bar

def extract_file(file_name, file_offset, file_length, mpk_name):
    output_folder = "results"
    output_path = os.path.join(output_folder, file_name)
    print("Extracting " + mpk_name + ": " + file_name + " (" + str(file_length) + " bytes)")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(mpk_name, "rb") as mpkfile:
        mpkfile.seek(file_offset)
        tmp = mpkfile.read(file_length)
        with open(output_path, "wb") as outfile:
            outfile.write(tmp)
    return output_path

def unpack_archive(mpkinfo_name, resource_files):
    progress_window, progress_bar = show_progress_bar()
    
    file = open(mpkinfo_name, "rb")
    file.read(4) # Skip the first 4 bytes (header)
    num_files = int.from_bytes(file.read(4), "little")

    for x in range(num_files):
        mpk_name = "Engine.mpk"
        name_length = int.from_bytes(file.read(2), "little")
        tmp = file.read(name_length)
        name = "".join(map(chr, tmp))
        file_offset = int.from_bytes(file.read(4), "little")
        file_length = int.from_bytes(file.read(4), "little")
        pak_index = int(int.from_bytes(file.read(4), "little") / 2)
        
        if resource_files:  # Verificar si resource_files no está vacía
            mpk_name = resource_files[min(pak_index, len(resource_files) - 1)]
        
        if file_length > 0:
            extract_file(name, file_offset, file_length, mpk_name)
            progress_bar.update((x + 1) * 100 / num_files)
    
    progress_window.close()

