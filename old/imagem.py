from PIL import Image
import shutil
import os

#user_input = input("Informe o diretorio onde estão localizados as imagens: ")
user_input = "/home/pedrosouza/Downloads/img-depois/JPG_nao_otimizadas/Convertidas_PNG/"
local = os.chdir(user_input)
itens = os.listdir()
itens_len = len(itens)

try:
    os.mkdir('Otimizadas')
    os.mkdir('NaoOtimizados')

except:
    pass

for i in itens:

    if ".jpeg" in i or ".png" in i or ".jpg" in i:
       
        try:
            print("Produto: "+i)
            image = Image.open(i)
            size = image.size
            new_size = []

            if size >= (1400, 1400):
                new_size = [(int((int(size[0])*35)/100)), (int((int(size[1])*35)/100))]
                image = image.resize((new_size[0], new_size[1]), Image.ANTIALIAS) 

            elif size >= (1000, 1000):
                new_size = [(int((int(size[0])*50)/100)), (int((int(size[1])*50)/100))]
                image = image.resize((new_size[0], new_size[1]), Image.ANTIALIAS) 

            elif size >= (800, 800):
                new_size = [(int((int(size[0])*75)/63)), (int((int(size[1])*63)/100))]
                image = image.resize((new_size[0], new_size[1]), Image.ANTIALIAS) 

            image.save(user_input+'Otimizadas/'+i,optimize=True,quality=85)

        except:
            print("Não movido: "+ i)
            shutil.copy(user_input+i, user_input+'NaoOtimizados/'+i)

    count_i = int(((itens.index(i))*100)/itens_len)
    print("Processando:", count_i,"%")
    
