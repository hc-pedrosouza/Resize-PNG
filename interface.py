import PySimpleGUI as gui
from os import error, path

def errorInterface(message, exc):
    gui.popup_error(message, exc, no_titlebar=True)

def progressBar(list_len):
    layout = [
        [gui.ProgressBar(max_value=list_len, orientation='h', size=(100, 50), key='progbar')],
        [gui.Cancel('Cancelar')]
    ]
    window = gui.Window('Redimensionar', layout, size=(200, 100), icon=False, resizable=False)
    event, values = window.read()


def mainInterface():
    user_input = {}

    layout = [
        [gui.Text("Informe novo valor de largura (altura será proporcionalmente redimensionada)")],
        [gui.Input(tooltip='Ex: 650.00', key='width',  )],
        [gui.Text()],
        [gui.Text('Informe pasta onde estão os arquivos')],
        [gui.Input(key='folder', tooltip='Ex: C:\\Users\\hcped\\Downloads\\Imagens'), gui.FolderBrowse('Procurar', )],
        [gui.OK('Redimensionar', button_color='green'), gui.Cancel('Cancelar', button_color='red')]
    ]

    window = gui.Window('Redimensionar', layout, size=(480, 180), resizable=True, icon=False)
    event, user_input = window.read()

    user_input.pop("Procurar")

    if event == 'Redimensionar':
        try:
            user_input['width'] = float(user_input['width'])
        except Exception as exc:
            errorInterface(message='Largura informada está no formato incorreto', exc=exc)
            return

        if not path.exists(user_input['folder']) and not path.isdir(user_input['folder']):
            errorInterface(message='Pasta selecionada é inválido ou inacessivel', exc=error.filename)
            return

        return user_input

if __name__ == '__main__':
    raise('Rodar setup.py')