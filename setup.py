#!/usr/bin/python3

import json
from pathlib import Path

# LOAD CONFIG FILES

path = Path(__file__).parent

configPath = str(path.joinpath('config/config.json'))
configFile = open(configPath, 'r', encoding='utf-8')
config = json.load(configFile)

envPath = str(path.joinpath('.env.example'))
envFile = open(envPath, 'r', encoding='utf-8')
env = envFile.read()

# INPUT: OUTLINE IP

defaultOutlineIP = config['inbounds'][0]['settings']['address']
if defaultOutlineIP == '<SERVER-IP>':
    message = "Outline Server Hostname:\n"
else:
    message = f"Outline Server Hostname: (Leave empty to use `{defaultOutlineIP}`)\n"

outlineIP = input(message)
if outlineIP == '':
    outlineIP = defaultOutlineIP

config['inbounds'][0]['settings']['address'] = outlineIP

# INPUT: OUTLINE PORT

defaultOutlinePort = config['inbounds'][0]['settings']['port']
outlinePort = input(f"Outline Server Port: (Leave empty to use `{defaultOutlinePort}`)\n")
if outlinePort == '':
    outlinePort = defaultOutlinePort

config['inbounds'][0]['settings']['port'] = int(outlinePort)

# SAVE CONFIG FILE

configContent = json.dumps(config, indent=2)
open(configPath, 'w', encoding='utf-8').write(configContent)

# SAVE ENV FILE
envContent = f"V2RAY_PORT={outlinePort}\n"
envPath = str(path.joinpath('.env'))
open(envPath, 'w', encoding='utf-8').write(envContent)

# PRINT OUT RESULT

print('Done!')
