import json
import os
ItemList = []
ChampList= []

myDir = 'Users\tolud\PycharmProjects\RiotTest\Champions 10.8.1'

class  Champion():
    def __init__(self, name, stats):
        self.name = name
        self.items = []
        self.maxItems = False
        self.stats = stats
    def getChamp(self):
        return self.name
    def AddItems(self):
        pass
    def MaxItems(self):#Set the max amount of Items that any champion can have
        if len(self.items) == 6:
            self.maxItems = True

class Items():
    def __init__(self, name, ):
        self.name = name

    def getItemName(self):
        return self.name

    def IsBoot(self):
        if self.name.index > -1:
            pass







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
    thisdir = '/Users/tolud/PycharmProjects/RiotTest/Champions 10.8.1'
    for file in os.listdir(thisdir):

        with open("Champions 10.8.1/" + file, "r") as j:
            data = json.load(j)
            champ = Champion(file[:-5], data["data"][file[:-5]]["stats"])
        ChampList.append(champ)




def CreateItems():
    with open("item.json", "r") as j: #opens the item.json file
        data = json.load(j)
    for item in data["data"]:
        item = Items(data["data"][item]["name"])

        ItemList.append(item)



CreateItems()

CreateChamps()


