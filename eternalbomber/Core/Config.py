from json import load, dump

VERSION = '1.0'

MY_COLOR = 'deeppurpleaccent100'

ENDWAY = 'https://endway.su/muqari'

CONFIG_NAME = 'config.json'



def check_config():

    while True:
        try:
            with open(CONFIG_NAME) as f:
                return load(f)
        except:
            with open(CONFIG_NAME, 'w') as f:
                f.write('{"theme": "dark", "feedback": "True", "type_attack": "MIX", "attack": "False", "key": "", "color": "deeppurpleaccent100"}')



def change_config(key, value):

    config = check_config()
    config[key] = f'{value}'
    with open(CONFIG_NAME, 'w') as f:
        dump(config, f)


