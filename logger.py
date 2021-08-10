import datetime

def successful(path, message):
    successful_path = path+'/Successful.log'
    date = str(datetime.datetime.now()).split('.')
    with open (successful_path, encoding='utf-8', mode='a') as file:
        file.write(f'{date[0]} | {message} \n')

def fail(path, message, e):
    fail_path = path+'/Fail.log'
    date = str(datetime.datetime.now()).split('.')
    with open (fail_path, encoding='utf-8', mode='a') as file:
        file.write(f'{date[0]} | {message} | {e} \n')