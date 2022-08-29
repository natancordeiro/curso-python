"""
 Manipulando arquivos
"""
import os 
import shutil

caminho_original = r"C:\Users\ncordeiro\Downloads\teste"
caminho_novo = r"C:\Users\ncordeiro\Downloads\teste\testando"

try: 
    os.mkdir(caminho_novo)
except FileExistsError as erro:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
         
        #movendo arquivos | Pode ser usado para renomear tbm
        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso.')

        #Copiando arquivos utilizando condicionais
        if '.txt' in file:
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso.')

        #Excluindo arquivos
        if '.txt' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} excluido com sucesso.')
    