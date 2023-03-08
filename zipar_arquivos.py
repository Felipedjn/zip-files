import os
import zipfile
import shutil
from time import sleep

def pastas_xml():
    
    diretorio_pasta = 'DIRETORIO/PASTA'

    #COMPILAÇÃO
    if len(os.listdir(diretorio_pasta)) == 0:
        pass
    else:
        files = os.listdir(diretorio_pasta)
        files_py = []

        for f in files:
            if f.endswith('xml'): #EXTENSAO DO ARQUIVO PRA COLOCAR NO ZIP
                fff = os.path.join(diretorio_pasta, f)
                files_py.append(fff)

        ZipFile = zipfile.ZipFile(f'{diretorio_pasta}.zip', 'w' )

        for a in files_py:
            ZipFile.write(a, 'C:\\' + os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)
        ZipFile.close()
        shutil.rmtree(diretorio_pasta)
        sleep(2)
        os.makedirs(diretorio_pasta)

pastas_xml()