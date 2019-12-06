import random
from collections import Counter

dropRates = ["1 - Rare"] * 55 + ["2 - Very Rare"] * 28 + ["3 - Import"] * 12 + ["4 - Exotic"] * 4 + ["5 - Black Market"] * 1
rare = ["Athena (Decal - Merc)", "Mosher (Decal - Imperator)", "Mister Monsoon (Decal - Jager)", "XVIII (Decal - Marauder)", "Funny Book (Decal - Dominus)"]
veryRare = ["Nipper (Wheels)", "Luminous (Trail)", "Ripped Comic (Decal - Octane)"] #only nipper can be painted
imp = ["Werewolf (Body)", "Tsunami Beam (Boost)", "Toon Sketch (Boost)"] 
exotic = ["Infinium (Wheels)", "Balla-Carra (Wheels)"]
bm = ["Chameleon (Univ. Decal)", "Storm Watch (Univ. Decal)", "Trigon (Univ. Decal)", "Toon (Goal Explosion)"] #none can be painted
paintCert = ["yes", "no", "no", "no"]
colors = ["Black", "Burnt", "Cobalt", "Crimson", "Green", "Grey", "Lime", "Orange", "Pink", "Purple", "Saffron", "Sky Blue", "Titanium White"]
certs = ["Acrobat", "Aviator", "Goalkeeper", "Gurdian", "Juggler", "Paragon", "Playmaker", "Scorer", "Show-Off", "Sniper", "Striker", "Sweeper", "Tactician", "Turtle", "Victor"]

totalCtr = Counter()
rarityCtr = Counter()
itemCtr = Counter()
itemWithPaintCtr = Counter()

def getItem():
    drop = random.choice(dropRates)
    paintable = "false"

    if drop == '1 - Rare':
        item = random.choice(rare)
        paintable = "true"
    elif drop == '2 - Very Rare':
        item = random.choice(veryRare)
        if item == "Nipper (Wheels)":
            paintable = "true"
    elif drop == '3 - Import':
        item = random.choice(imp)
        paintable = "true"
    elif drop == '4 - Exotic':
        item = random.choice(exotic)
        paintable = "true"
    else:
        item = random.choice(bm)

    cert = random.choice(paintCert)
    if cert == "yes":
        certification = random.choice(certs)
        certItem = item + " - Cert: " + certification

    paintedItem = item
    paintedOnlyItem = item
    if paintable == "true":
        paint = random.choice(paintCert)
        if paint == "yes":
            paintFinish = random.choice(colors)
            paintedItem = paintedItem + " - Paint: " + paintFinish
            paintedOnlyItem = paintedItem + " - Paint: " + paintFinish
            if cert == "yes":
                paintedItem = certItem + " - Paint: " + paintFinish

    totalCtr[drop + " -- " + paintedItem] += 1
    rarityCtr[drop] += 1
    itemCtr[drop + " -- " + item] += 1
    itemWithPaintCtr[drop + " -- " + paintedOnlyItem] += 1


i=0
while i < 10000:
    getItem()
    i+=1

totalResultsDict = dict(totalCtr)
rarityDict = dict(rarityCtr)
itemDict = dict(itemCtr)
itemWithPaintDict = dict(itemWithPaintCtr)


totalResults = open('totalResults.txt', 'w') 
rarityResults = open('rarityResults.txt', 'w') 
itemResults = open('itemResults.txt', 'w') 
itemWithPaintResults = open('itemWithPaintResults.txt', 'w') 


for key in sorted(totalResultsDict.keys()):
    print("%s: %s" % (key, totalResultsDict[key]), file = totalResults)

for key in sorted(rarityDict.keys()):
    print("%s: %s" % (key, rarityDict[key]), file = rarityResults)

for key in sorted(itemDict.keys()):
    print("%s: %s" % (key, itemDict[key]), file = itemResults)

for key in sorted(itemWithPaintDict.keys()):
    print("%s: %s" % (key, itemWithPaintDict[key]), file = itemWithPaintResults)


totalResults.close() 
rarityResults.close() 
itemResults.close() 
itemWithPaintResults.close() 

# sortedSetList = sorted(setList)
# print(sortedSetList)

