import interface as Interface
import logger as Logger
from PIL import Image
from os import mkdir, chdir, listdir, remove

class ImageResize():
    def __init__(self, new_width, path):
        self.new_width = int(new_width)
        self.path = path
        self.list_images = []
        self.otimizados = '/Otimizados/'

    def resize(self):
        chdir(self.path)
        #TODO:
        #https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-custom-progress-meter-progress-bar
        for current_file in self.list_images:
            try:
                image = Image.open(current_file)
                width, height = image.size
                new_height = int((height*(((self.new_width*100)/width)))/100)

                image = image.resize((self.new_width, new_height), Image.ANTIALIAS)
                image.save(self.path+self.otimizados+current_file, optimize=True, quality=85)

                message = f'{current_file} redimensionado de {width}x{height} para {self.new_width}x{new_height}'
                Logger.successful(self.path, message)

            except Exception as e:
                message = f'{current_file} erro ao tentar redimensionar e salvar'
                Logger.fail(self.path, message, e)


    def makeFolder(self):
        try:
            mkdir(self.path+self.otimizados)
        except:
            return('Não foi possivel criar as pastas')

        return ('Pastas Criadas com Sucesso!')
        
    def getFiles(self):
        try:
            list_all = listdir(self.path)
            list_images = []
            for item in list_all:
                if '.png' in item:
                    list_images.append(item)
            self.list_images = list_images
        except:
            return('Não foi possivel listar os arquivos')

        return 'Listados com Sucesso!'
        


if __name__ == '__main__':
    interface = Interface.mainInterface()
    if interface == None:
        pass
    else:
        image_resize = ImageResize(interface['width'], interface['folder'])
        image_resize.getFiles()
        image_resize.makeFolder()
        image_resize.resize()
    