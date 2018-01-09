import MongoDBConnect
import re

def durationOneQuerry(entity,client):
    duration =""
    # db connection
    #client = MongoDBConnect.mongoConnect()
    # db querry
    doc = client.find({"attractionName": entity})
    #duration = doc.suggestedDuration
    for document in doc:
       duration = document["suggestedDuration"]
    reply = "It will take "+ duration + " to visit "+ entity
    print(reply)

def durationTwoQuery(entity,question,client):
    # execute query
    suggestedDuration = ""
    # db query
    doc = client.find({"attractionName": entity})
    # duration = doc.suggestedDuration
    for document in doc:
        suggestedDuration = document["suggestedDuration"]
    print(suggestedDuration)
    hrs = getDuration(question)
    print(hrs)
    answer = ''
    if(len(hrs) == 1):
        answer = getAnswerLengthOne(question,hrs,suggestedDuration)
    print(answer)

def getDuration(question):
    regex = r"((take|cover|going|finish).*((\d(\s)*(-|to|/)(\s)*)*(\d) hours|minutes).*)"
    cardinalityWithUnits = re.search(regex,question).group(3)
    #print(cardinalityWithUnits)
    cardinality = re.findall('\d+',cardinalityWithUnits)    #['2', '3']
    #print(cardinality)
    #print(cardinality[0])
    first, *middle, last = cardinalityWithUnits.split()
    units = last
    #print(units)
    # get exact unit
    unit = getExactUnit(units)
    #print(unit)
    hrs = [2]
    # cardinality only 1 number
    if(len(cardinality) == 1):
        if(unit == 'minutes'):
            hrs[0] = int(cardinality[0])/60
        else:
            hrs[0] = int(cardinality[0])
    elif(len(cardinality) == 2):
        if (unit == 'minutes'):
            hrs[0] = int(cardinality[0]) / 60
            hrs[1] = int(cardinality[1]) / 60
        else:
            hrs[0] = int(cardinality[0])
            hrs[1] = int(cardinality[1])
    return hrs

def getExactUnit(unit):
    units = ''
    unit = unit.lower()
    if(unit == 'hours' or unit == 'hrs' or unit == 'hour' or unit == 'hr'):
        units = 'hours'
    elif(unit == 'minutes' or unit == 'mins' or unit == 'minute' or unit == 'min'):
        unit = 'minutes'
    else:
        unit = 'UNIT_ERROR'
    return unit

def getAnswerLengthOne(question,hrs,suggestedDuration):
    noOfHrs = hrs[0]
    if('less than' in suggestedDuration):
        sugHrsArray = re.findall('\d+',suggestedDuration)    #['2', '3']
        if(len(sugHrsArray) == 1):
            if('less than' in question):
                if(noOfHrs <= int(sugHrsArray[0])):
                    return 'Yes, it will take ' + suggestedDuration
                else:
                    return 'No, it will take ' + suggestedDuration
            elif ('more than' in question):
                if (noOfHrs <= int(sugHrsArray[0])):
                    return 'No, it will take ' + suggestedDuration
                else:
                    return 'Yes, it will take ' + suggestedDuration
            else:
               return 'It will take ' + suggestedDuration