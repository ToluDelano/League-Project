import json
import os
ItemList = []


class  Champion():
    def __init__(self, name):
        self.name = name
        self.items = []
    def getChamp(self):
        return self.name

class Items():
    def __init__(self, name, keyCode):
        self.name = name
        self.keyCode = keyCode
    def getItemName(self):
        return self.name

    def IsBoot(self):
        if self.name.index > -1:
            pass

    def getItemKeyCode(self):
        return self.keyCode





def ReadItems():

    with open("item.json", "r") as j:
        data = json.load(j)
    with open("response.json", "w") as f:
        json.dump(data, f, indent=4)

    items = []
    items_Stat_Type = []
    items_stats = []

    for key in data['data']:
        items.append(data['data'][key]['name'])
        #print(data['data'][key]['name'])

    print(items[0])



def ReadbleChamp():

    with open("Champions 10.8.1/Aatrox.json", "r") as j:
        data = json.load(j)
    with open("ReadbleChamp.json", "w") as f:
        json.dump(data, f, indent=4)


    for key in data['data']['Aatrox']['stats']:
        print(data['data']['Aatrox']['stats'][key])
def CreateChamps():
    pass
def CreateItems():
    with open("item.json", "r") as j: #opens the item.json file
        data = json.load(j)
    for item in data["data"]:
        item = Items(data["data"][item]["name"], str(data["data"][item].keys))

        ItemList.append(item)


CreateItems()

for item in ItemList:
    print(item.keyCode)


