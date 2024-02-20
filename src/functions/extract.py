import os

def extract_file(file_name, file_offset, file_length, mpk_name, output_dir, file_format=None):
    output_folder = output_dir + "/results"
    output_path = os.path.join(output_folder, file_name)
    
    # Verificar si se especificó un formato de archivo
    if file_format:
        # Obtener la extensión del archivo
        file_extension = os.path.splitext(file_name)[1].lower()
        
        # Si la extensión del archivo no coincide con el formato especificado, no extraer el archivo
        if file_extension not in file_format:
            print(f"Skipping {file_name} (not in specified format: {file_format})")
            return None

    print("Extracting " + mpk_name + ": " + file_name + " (" + str(file_length) + " bytes)")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(mpk_name, "rb") as mpkfile:
        mpkfile.seek(file_offset)
        tmp = mpkfile.read(file_length)
        with open(output_path, "wb") as outfile:
            outfile.write(tmp)
            
    return output_path