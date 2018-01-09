import nltk
import re
import MongoDBConnect
import patternDuration
import patternOpenHours
import patternImportance
import patternSuggestion
from nltk import word_tokenize

class semantic_match:
 regduone = r"(long.*(view|look|see))"
 regdutwo = r"((\d.*\d) (hours|minutes))|((\d) (hours|minutes))"
 regopenhours = r"(open)"
 regopendays = r"(open on .*)"
 regseasonone = r"(season)"
 regseasontwo = r"(best time .* (visit)* )"
 regreserveone = r"((purchase|buy|book).*(advance|beforehand|early))"
 regreservetwo = r"((reserve|order|reservation))"
 regaudkids = r"((safe) .* (kids))"
 regaccessbility = r"(handicap.* (visit|come|))"
 regaudience = r"((ideal|suitable|good) for (.*))"
 regalloweditems = r"(bring|take|allow.*)"
 regimportance = r"(import.*|signifi.*|famous.* (^places))"
 regsuggest = r"((famous|popular)* .*(places|attractions).*(in(.*)))"
 regactivities = r"((do|engage) (in (.*)))"
 regequipment = r"((provide(d)*|give(n)*).*)"
 regbusyone = r"((what day(s)*|when|time).*crowded.*)"
 regbusytwo = r"(crowded.*(day(s)*|pm|am))"
 regbusythree = r"((at) (\d).*(crowded))"

 chat = {'CurrentEntity':[],'Duration':[],'OpenHours':[],'OpenDays':[],'Season':[],
                 'Audience':[],'Reserve':[],'AllowedItems':[],
                 'Importance':[],'Suggestions':[],'Activites':[],'Equipment':[]}
 chat_history =[]


 def reg_match(question, entity, dbConnect):
  if(re.search(semantic_match.regduone, question, flags=0)):
    # matching regex duration one
    patternDuration.durationOneQuerry(entity , dbConnect)
  elif(re.search(semantic_match.regdutwo, question, flags=0)):
   # matching regex duration comparison
   patternDuration.durationTwoQuery(entity, question, dbConnect)
  elif(re.search(semantic_match.regopendays, question, flags=0)):
   patternOpenHours.openDaysQuery(entity, client)
  elif(re.search(semantic_match.regopenhours, question, flags=0)):
   patternOpenHours.openDaysQuery(entity, client)
  elif(re.search(semantic_match.regseasonone, question, flags=0)):
   print("The season is from March to May")
  elif (re.search(semantic_match.regseasontwo, question, flags=0)):
   print("April is the best time to visit")
  elif (re.search(semantic_match.regreserveone, question, flags=0)or
        re.search(semantic_match.regreservetwo, question, flags=0)):
   print("You have to book in advance")
  elif (re.search(semantic_match.regaudkids, question)):
   print("Yes you can bring kids")
  elif (re.search(semantic_match.regaccessbility, question)):
   print("Handicapeed people can visit")
  elif (re.search(semantic_match.regaudience, question)):
   print("It is suitable for" + re.search(semantic_match.regaudience, question).group(3))
  elif (re.search(semantic_match.regalloweditems, question)):
   item = semantic_match.get_item(question)
   print("Yes it is allowed inside")# hv to extract the name of the item asked about
  elif (re.search(semantic_match.regimportance, question)):
   patternImportance.importanceQuery(entity,client)
  elif (re.search(semantic_match.regsuggest, question)):

   print("You can visit the museum and the palace")
  elif (re.search(semantic_match.regactivities, question)):
   print("You can do scuba diving")
  elif (re.search(semantic_match.regequipment, question)):
   print("It will be provided at the museum")



 def part_of_seech(str):
  text = word_tokenize(str)
  tagged = nltk.pos_tag(text)
  print(tagged)
  grammar = r"""
    NP: {<JJ>+<NN>+}            #chunk determiner/possessive, adjectives and noun
        {<NNP>+<CC>?<NNP|NN>*}   #chunk sequences of proper nouns followed by zero or more nouns
        {<NN><IN>*<NNP>}        #museum of London

  """
  chunker = nltk.RegexpParser(grammar)
  tree = chunker.parse(tagged)
  phrase = []
  for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
   phrase.append(subtree.leaves())

  return phrase

 def get_item(str):
  text = word_tokenize(str)
  tagged = nltk.pos_tag(text)
  for item in tagged:
   if(item[1] == 'NN'):
    return item[0]

#nltk.download()
client = MongoDBConnect.mongoConnect().AttractionDetails.Attraction
#patternDuration.durationTwoQuery("Charles Bridge","1 hour")
while(True):
 #get input
 question= input()
 #get entity
 entity = semantic_match.part_of_seech(question)
 s = ""
 i = 1

 for list in entity:
  for item in list:
   if(i!=len(list)):
    s += item[0]+ " "
   else:
    s+= item[0]
   i = i + 1

 if (len(s) != 0):
  print(s)
  #call regexes
  semantic_match.reg_match(question, s, client)
  semantic_match.chat_history.append(s)
 else:
  print("No entity")
  if(len(semantic_match.chat_history)!=0):
   entity = max(semantic_match.chat_history)
   semantic_match.reg_match(question,entity, client)


