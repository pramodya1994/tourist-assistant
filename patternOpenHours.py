
def openDaysQuery(entity, client):
    openHours = ""

    # db querry
    doc = client.find({"attractionName": entity})

    for document in doc:
     duration = document["openHours"]

    i=0
    for key, value in duration.items():
     i+=1
     if(len(duration.items())>1 and len(duration.items())!=i):
       openHours += key + " from " + value+" and "
     else:
       openHours += key + " from " + value

    print("The "+entity+" will be open on "+ openHours)