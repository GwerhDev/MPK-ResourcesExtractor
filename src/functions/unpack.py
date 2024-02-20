from src.functions.progressbar import show_progress_bar
from src.functions.extract import extract_file

def unpack_archive(mpkinfo_name, output_dir, resource_files, file_format=None):
    progress_window, progress_bar = show_progress_bar()
    file = open(mpkinfo_name, "rb")
    
    # Skip the first 4 bytes (header)
    file.read(4)
    num_files = int.from_bytes(file.read(4), "little")

    for x in range(num_files):
        mpk_name = "Engine.mpk"
        name_length = int.from_bytes(file.read(2), "little")
        tmp = file.read(name_length)
        name = "".join(map(chr, tmp))
        file_offset = int.from_bytes(file.read(4), "little")
        file_length = int.from_bytes(file.read(4), "little")
        pak_index = int(int.from_bytes(file.read(4), "little") / 2)
        
        # Check if resource_files is not empty
        if resource_files:  
            mpk_name = resource_files[min(pak_index, len(resource_files) - 1)]
        
        if file_length > 0:
            # Pasar el formato de archivo a la función extract_file si está especificado
            if file_format:
                extract_file(name, file_offset, file_length, mpk_name, output_dir, file_format=file_format)
            else:
                extract_file(name, file_offset, file_length, mpk_name, output_dir)
            progress_bar.update((x + 1) * 100 / num_files)
    
    progress_window.close()
