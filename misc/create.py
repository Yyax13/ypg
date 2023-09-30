from misc import loading as Carregante
import os as MInT
def create_archive(content, arqName, ext, ProjPath):
    caminho_completo = f"{ProjPath}/{arqName}.{ext}"
    LoadingText = f'Criando o arquivo {arqName}.{ext} em {caminho_completo}'
    
    if not MInT.path.exists(f"{ProjPath}"):
        MInT.makedirs(f"{ProjPath}")
    
    try:
        with open(caminho_completo, 'w') as arquivo:
            arquivo.write(content)
            Carregante.start(texto=LoadingText, NV=2)
    except Exception as e:
        print(f"Ocorreu um erro ao escrever o arquivo: {str(e)}")