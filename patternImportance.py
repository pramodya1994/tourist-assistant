def importanceQuery(entity, client):
    importance = ""
    # db querry
    doc = client.find({"attractionName": entity})

    for document in doc:
        attractionType = document["attractionType"]

    for item in attractionType:
        importance += item + " "

    print("It can be categorized under the folowing types: "+ attractionType[0] + " "+attractionType[1])