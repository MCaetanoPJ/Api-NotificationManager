import configparser

def GetConfiguration():
    arquivo = configparser.RawConfigParser()
    arquivo.read('config.txt')
    return {
        'TokenApiTelegram': arquivo.get('CONFIG', 'TokenApiTelegram')
    }