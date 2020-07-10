import json
ItemList = []
ChampList = []


class Champion:
    def __init__(self, name, stats):
        self.name = name
        self.items = []
        self.maxItems = False
        self.stats = stats

    def getchamp(self):
        return self.name

    def getstats(self):
        return self.stats

    def additems(self, additem):
        if len(self.items) < 6:
            with open("StatMap.json", "r") as j:
                data = json.load(j)
            for item in ItemList:
                if item.getitemname() == additem:  # and (self.maxItems == False):
                    self.items.append(item)
                    for ItemStatKey in item.stats.keys():
                        for ChampStatKey, ChampStat in self.stats.items():  # iterate the stat that each item gives
                            if ChampStatKey == data["stats"][ItemStatKey]:
                                self.stats[ChampStatKey] += item.stats[ItemStatKey]
                                break

    def addlevel(self):
        self.stats["hp"] += self.stats["hpperlevel"]
        self.stats["mp"] += self.stats["mpperlevel"]
        self.stats["armor"] += self.stats["armorperlevel"]
        self.stats["spellblock"] += self.stats["spellblockperlevel"]
        self.stats["hpregen"] += self.stats["hpregenperlevel"]
        self.stats["mpregen"] += self.stats["mpregenperlevel"]
        self.stats["crit"] += self.stats["critperlevel"]
        self.stats["attackdamage"] += self.stats["attackdamageperlevel"]
        self.stats["attackspeed"] += self.stats["attackspeedperlevel"]

    def getitemlist(self):
        return self.items


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
    with open("champion.json", "r", encoding="utf8") as j:
        data = json.load(j)
        for key in data["data"]:
            champ = Champion(data["data"][key], data["data"][key]["stats"])
            ChampList.append(champ)


def createitems():
    with open("item.json", "r") as j:  # opens the item.json file
        data = json.load(j)
        keylist = list(data["data"].keys())
    for index, item in enumerate(keylist):
        item = Items(keylist[index], data["data"][item])
        ItemList.append(item)


def searchitems(itemname, itemlist):
    for obj in itemlist:
        if obj.getitemname() == itemname:
            return obj


def searchchamp(champname, champlist):
    for obj in champlist:
        if obj.getchamp() == champname:
            return obj


def compare(champ1, champ2):
    pass

createchamps()
createitems()
print(ChampList[0].getstats())
# ChampList[0].additems("Pickaxe")
Champion.addlevel(ChampList[0])
print(ChampList[0].getstats())


#print(searchchamp("Aatrox", ChampList))