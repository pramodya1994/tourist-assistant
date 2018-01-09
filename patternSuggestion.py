def suggestionQuery(entity,client):
    suggestion=""
    #db= client.AttractionDetails
    client.create_index([('address', 'text')])

    doc = client.find({"$text": {"$search": "Prague"}})
    for document in doc:
        suggestion = document["attractionName"]
        print(suggestion)

