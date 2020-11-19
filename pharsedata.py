import json
with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

#-------------------------------------------------------------------------------
obama = 0
for i in jsonData:
    if "obama" in i['tweet'].lower():
        obama += 1

print ("Jimmy fallon mentions Obama:", obama, " times")
#-------------------------------------------------------------------------------
tyNotes = 0;

for i in jsonData:
    if "#thankyounotes" in i['tweet'].lower():
        tyNotes += 1

print ("Jimmy fallon tweets about thank you notes:", tyNotes, " times")
#-------------------------------------------------------------------------------

dates=[]
for i in jsonData:
    dates.append(i['date'])

with open('Dates.json','w') as out:
    json.dump(dates,out,indent=2)
