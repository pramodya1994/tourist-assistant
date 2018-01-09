def audienceKidsQuery(entity,client):
    audience = []
    doc = client.find({"attractionName": entity})

    for document in doc:
     audience = document["audience"]

    for item in audience:
     if("Kids" in item or "Family"):
         print( entity+" is ok for kids to visit")

def audienceQuery(entity,client):
    audience = []
    category = ""
    doc = client.find({"attractionName": entity})

    for document in doc:
        audience = document["audience"]

    for item in audience:
     category += item + ", "
    print(entity + " is ok for"+ category + "to visit")