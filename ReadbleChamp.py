import os
import json

with open("Champions 10.8.1/Aatrox.json", "r") as j:
    data = json.load(j)
with open("ReadbleChamp.json", "w") as f:
    json.dump(data, f, indent=4)

stats = []

for key in data['data']['Aatrox']['stats']:
    print(data['data']['Aatrox']['stats'][key])

