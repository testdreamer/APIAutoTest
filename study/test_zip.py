import zipfile
import os
from Utils.zip_file import make_zip

source_filename = os.path.dirname(__file__)+'/data/test_zip'
out_filename = os.path.dirname(__file__)+'/data/test_zip.zip'
# zipfile.ZipFile(file=out_filename, mode='w')

for father, dirname, filenames in os.walk(source_filename):
    for filename in filenames:
        pathfile = os.path.join(father, filename)
        # print(pathfile)
        print(pathfile[34:].strip(os.path.sep))
        zipf.write(pathfile, arcname)

# make_zip(source_filename, out_filename)

# print(source_filename)
# print(len(source_filename))