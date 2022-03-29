f = open("fileone.txt", "w+")
f.write("ONE FILE")
f.close()

f = open("filetwo.txt", "w+")
f.write("TWO FILE")
f.close()

import zipfile
import os

comp_file = zipfile.ZipFile("comp_file.zip", "w")
comp_file.write("fileone.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filetwo.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
zip_obj = zipfile.ZipFile("comp_file.zip", "r")
zip_obj.extractall("extracted_content")

import shutil

dir_to_zip = str(os.getcwd()) + "/extracted_content"
output_filename = 'example'
shutil.make_archive(output_filename, "zip", dir_to_zip)
shutil.unpack_archive("example.zip", "final_zip", "zip")