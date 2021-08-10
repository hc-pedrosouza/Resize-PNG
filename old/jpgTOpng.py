from PIL import Image
import os
import shutil

user_input = "/home/pedrosouza/Downloads/img-depois/JPG_nao_otimizadas/"
local = os.chdir(user_input)
itens = os.listdir()
itens_len = len(itens)

try:
    os.mkdir("Convertidas_PNG")
    os.mkdir("Nao_Convertidas")

except:
    pass

for i in itens:

    if ".jpg" in i:
        print("Produto: "+i)
        splited = i.split(".")

        try:
            image = Image.open(i)
            image.save("/home/pedrosouza/Downloads/img-depois/JPG_nao_otimizadas/Convertidas_PNG/"+str(splited[0])+".png")

        except:
            shutil.copy("/home/pedrosouza/Downloads/img-depois/JPG_nao_otimizadas/"+i,"/home/pedrosouza/Downloads/img-depois/JPG_nao_otimizadas/Nao_Convertidas/"+i)

    count_i = int(((itens.index(i))*100)/itens_len)
    print("Processando:", count_i,"%")