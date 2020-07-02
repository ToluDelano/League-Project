import json
import os
ItemList = []
ChampList= []

myDir = 'Users\tolud\PycharmProjects\RiotTest\Champions 10.8.1'



class Champion():
    def __init__(self, name, stats):
        self.name = name
        self.items = []
        self.maxItems = False
        self.stats = stats
    def getChamp(self):
        return self.name
    def getStats(self):
        return self.stats



    def AddItems(self, item):

        with open("StatMap.json", "r") as j:
            data = json.load(j)

        for thing in ItemList:
            if (thing.getItemName() == item): #and (self.maxItems == False):
                self.items.append(thing)
                for ItemStatKey in thing.stats.keys():
                    for ChampStatKey, ChampStat in self.stats.items():  # iterate the stat that each item gives
                        if ChampStatKey == data["stats"][ItemStatKey]:
                           self.stats[ChampStatKey] += thing.stats[ItemStatKey]
                           break




    def getItemList(self):
        return self.items




    def MaxItems(self):#Set the max amount of Items that any champion can have
        if len(self.items) == 6:
            self.maxItems = True

class Items():
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def getItemName(self):
        return self.name

    def IsBoot(self):
        if self.name.index > -1:
            pass

    def getItemStats(self):
        return self.stats






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






def CreateChamps():
    thisdir = '/Users/tolud/PycharmProjects/RiotTest/Champions 10.8.1'
    for file in os.listdir(thisdir):

        with open("Champions 10.8.1/" + file, "r", encoding="mbcs") as j:
            data = json.load(j)
            champ = Champion(file[:-5], data["data"]["stats"])
        ChampList.append(champ)




def CreateItems():
    with open("item.json", "r") as j: #opens the item.json file
        data = json.load(j)
        keylist = list(data["data"].keys())

    for index, item in enumerate(keylist):
        item = Items(keylist[index], data["data"][item])

        ItemList.append(item)

def SearchItems(itemName, itemList):
    for obj in itemList:
        if obj.getItemName() == itemName:
            return obj

def SearchChamp(champName, Champlist):
    for obj in ChampList:
        if obj.getChamp() == champName:
            return obj

def Compare(Champ1, Champ2):
    pass

CreateItems()

CreateChamps()

#print(ChampList[0].getStats())
#ChampList[0].AddItems("Pickaxe")

#print(ChampList[0].getStats())


print(SearchChamp("Aatrox", ChampList))
