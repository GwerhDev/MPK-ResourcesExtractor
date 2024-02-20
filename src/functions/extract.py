import os

def extract_file(file_name, file_offset, file_length, mpk_name, output_dir):
    output_folder = output_dir + "/results"
    output_path = os.path.join(output_folder, file_name)
    print("Extracting " + mpk_name + ": " + file_name + " (" + str(file_length) + " bytes)")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(mpk_name, "rb") as mpkfile:
        mpkfile.seek(file_offset)
        tmp = mpkfile.read(file_length)
        with open(output_path, "wb") as outfile:
            outfile.write(tmp)
    return output_path