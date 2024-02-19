import sys
import os

# Extracts the file from the MPK file
def extract_file(file_name, file_offset, file_length, mpk_name):
    print("Extracting " + mpk_name + ": " + file_name + " (" + str(file_length) + " bytes)")
    mpkfile = open(mpk_name, "rb")
    mpkfile.seek(file_offset)
    tmp = mpkfile.read(file_length)
    mpkfile.close()
    outfile = open(file_name, "wb")
    outfile.write(tmp)
    outfile.close()

def list_archive_contents(mpkinfo_name, resource_info, resource_files):
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
        if(sys.argv[1] == resource_info):
            mpk_name = resource_files[pak_index]
        if(file_length > 0):
            print(mpk_name + ": " + name + ", length: " + str(file_length) + " bytes, offset: " + str(file_offset))

def unpack_archive(mpkinfo_name, resource_files):
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
        mpk_name = resource_files[pak_index]
        if(file_length > 0):
            try:
                os.makedirs(os.path.dirname(name))
            except FileExistsError:
                pass

            extract_file(name, file_offset, file_length, mpk_name)
