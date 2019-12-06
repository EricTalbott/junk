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

ctr = Counter()

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

    if paintable == "true":
        paint = random.choice(paintCert)
        if paint == "yes":
            paintFinish = random.choice(colors)
            item = item + " - Paint: " + paintFinish

    cert = random.choice(paintCert)
    if cert == "yes":
        certification = random.choice(certs)
        item = item + " - Cert: " + certification

    ctr[drop + " -- " + item] +=1


i=0
while i < 10000:
    getItem()
    i+=1

dictList = dict(ctr)


sample = open('results.txt', 'w') 
for key in sorted(dictList.keys()):
    print("%s: %s" % (key, dictList[key]), file = sample)
sample.close() 

# sortedSetList = sorted(setList)
# print(sortedSetList)

