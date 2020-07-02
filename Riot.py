import json
import os
ItemList = []
ChampList = []

myDir = os.getcwd() + '\Champions 10.8.1'


<<<<<<< HEAD

class Champion():
=======
class Champion:
>>>>>>> bda6ae2dd7c69d80f8a584ac376e7af75ee5f6e8
    def __init__(self, name, stats):
        self.name = name
        self.items = []
        self.maxItems = False
        self.stats = stats

    def getchamp(self):
        return self.name

    def getstats(self):
        return self.stats

    def additems(self, item):
        with open("StatMap.json", "r") as j:
            data = json.load(j)
        for thing in ItemList:
            if thing.getitemname() == item:  # and (self.maxItems == False):
                self.items.append(thing)
                for ItemStatKey in thing.stats.keys():
                    for ChampStatKey, ChampStat in self.stats.items():  # iterate the stat that each item gives
                        if ChampStatKey == data["stats"][ItemStatKey]:
                            self.stats[ChampStatKey] += thing.stats[ItemStatKey]
                            break

    def getitemlist(self):
        return self.items

    def maxitems(self):  # Set the max amount of Items that any champion can have
        if len(self.items) == 6:
            self.maxItems = True


class Items:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def getitemname(self):
        return self.name

    def isboot(self):
        if self.name.index > -1:
            pass

    def getitemstats(self):
        return self.stats


def readitems():
    items = []
    items_stat_type = []
    items_stats = []

    with open("item.json", "r") as j:
        data = json.load(j)
    with open("response.json", "w") as f:
        json.dump(data, f, indent=4)
    for key in data['data']:
        items.append(data['data'][key]['name'])
        # print(data['data'][key]['name'])
    print(items[0])


def createchamps():
    thisdir = os.getcwd() + '/Champions 10.8.1'
    for file in os.listdir(thisdir):
        with open("Champions 10.8.1/" + file, "r", encoding="mbcs") as j:
            data = json.load(j)
            champ = Champion(file[:-5], data["data"]["stats"])
        ChampList.append(champ)


def createitems():
    with open("item.json", "r") as j:  # opens the item.json file
        data = json.load(j)
        keylist = list(data["data"].keys())
    for index, item in enumerate(keylist):
        item = Items(keylist[index], data["data"][item])
        ItemList.append(item)

<<<<<<< HEAD
def SearchItems(itemName, itemList):
    for obj in itemList:
        if obj.getItemName() == itemName:
            return obj

def SearchChamp(champName, Champlist):
    for obj in ChampList:
        if obj.getChamp() == champName:
            return obj
=======

def searchitems():
    pass
>>>>>>> bda6ae2dd7c69d80f8a584ac376e7af75ee5f6e8


def searchchamp():
    pass


def compare(champ1, champ2):
    pass

<<<<<<< HEAD
#print(ChampList[0].getStats())
#ChampList[0].AddItems("Pickaxe")

#print(ChampList[0].getStats())


print(SearchChamp("Aatrox", ChampList))
=======

createitems()
createchamps()
#
print(ChampList[0].getstats())
ChampList[0].additems("Pickaxe")
#
print(ChampList[0].getstats())
>>>>>>> bda6ae2dd7c69d80f8a584ac376e7af75ee5f6e8
