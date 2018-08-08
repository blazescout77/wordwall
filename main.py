import json
from random import randint

any_file = open("mySavedDict.txt","r",encoding="utf-8")
everything = json.load(any_file)


def startup():
  """What else the name tells you all, this function boots the program up and gears it for the wordwall, if this fails the enitre program is unusable so this a a very key part to the program

  simply input startup()
  to start the program

  """
  print("Hello there lets start using your word wall\n")
  print("Learning a new word a day goes a long way in helping to expand your vocabulary :)\n")
  answername = input("Are you a new user (yes/no)\n")
  if answername == "yes":
    newname = input("What do you want for your username?")
    everything[newname]={}
    updated = json.dumps(everything)
    ten_file = open("mySavedDict.txt","w",encoding="utf-8")
    ten_file.truncate(0)
    ten_file.write(updated)
    ten_file.close()
    print("please restart function to enable functions")
    goagain()
  elif answername == "no":
    existingname = input("Whats your username?")
    print('Aivailable functions: \n (new word/delete word/edit/view/pop quiz/help)')
    function = input("What would you like to do?")
    if function == "new word":
      addnewword(existingname)
    elif function == 'delete word':
      deleteword(existingname)
    elif function == 'edit':
      edit(existingname)
    elif function == "view":
      view(existingname)
    elif function =="pop quiz":
      popquiz(existingname)
    elif function == "help":
      print("Type help(function)")
      pass
    else:
      print("Invalid command please try again")
      startup()
  else:
    print("Please yes or no not anything else no caps")
    startup()


def addnewword(user):
  """Allows user to add new words to word wordwall

  Enter new word when prompt what would you like to do is given

  """
  numbercheck = 0
  for person, theirdictionary in everything.items():
    if person == user:
      numbercheck += 1
      newword = input("Whats the newword you want to learn")
      wordcheck(newword,person)
      meaning = input("Whats the meaning of the word")
      definitioncheck(meaning,person)
      for word,itsmeaning in theirdictionary.items():
          if word == newword:
            print("You already have this word in your word wall")
            addnewword(user)
      theirdictionary[newword]=meaning
      updated = json.dumps(everything)
      t = open("mySavedDict.txt","w")
      t.truncate(0)
      t.write(updated)
      t.close()
      goagain()
  if numbercheck == 0:
    print("Pleae lah no results leh, try again")
    startup()

def deleteword(user):
  """Allows user to delete word of choice
  
  words keyed in are case sensitive, hence exact word needs to be keyed in when prompted to, function may not work if word is capped 

  Only allowed for existing users
  """
  for person, theirdictionary in everything.items():
    if person == user:
      print("here is the words you have learnt")
      for word, meaning in theirdictionary.items():
        print("word ", word,":","meaning ",meaning)
  numbercheck = 0
  for person, theirdictionary  in everything.items():
    if person == user:
      numbercheck += 1
      wanttodelete = input("Which word would you like to delete")
      try:
        del theirdictionary[wanttodelete]
      except:
        print("Word not found try again")
        deleteword(user)
      updated = json.dumps(everything)
      t = open("mySavedDict.txt","w")
      t.truncate(0)
      t.write(updated)
      t.close()
      goagain()
  if numbercheck == 0:
    print("no results found try again")
    startup()

def edit(user):
  """Allows user to edit exisitng word meanings 

  Users are allowed to do so by keying in the word and the new meaning

  only allowed for exisiting users

  """
  numbercheck = 0
  for person, theirdictionary in everything.items():
    if person == user:
      numbercheck += 1
      wanttoedit = str(input("Which word do you want to edit?"))
      try:
        del theirdictionary[wanttoedit]
      except:
        print("Not found try again")
        edit(user)
      newmeaning = input('Whats the edited meaning')
      definitioncheck(newmeaning,user)
      try:
        theirdictionary[wanttoedit] = newmeaning
      except:
        print("Not found, try again")
        edit(user)
      updated = json.dumps(everything)
      t = open("mySavedDict.txt","w")
      t.truncate(0)
      t.write(updated)
      t.close()
      goagain()
  if numbercheck == 0:
    print("No results found")
    startup()

def view(user):
  """Allows user to view all of existing words and meanings

  only allowed for exisiting users
  """
  numbercheck = 0
  for person, theirdictionary in everything.items():
    if person == user:
        numbercheck += 1
        print("here is the words you have learnt")
        for word, meaning in theirdictionary.items():
          print("word ", word,":","meaning ",meaning)
  if numbercheck == 0:
    print("No results found, try again")
    startup()
  goagain()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

def goagain():
  """Allows user to go again can be placed in functions
  """
  response = input("go again? (yes/no)")
  if response == "yes":
    startup()
  if response == "no":
    pass
  else:
    print("Huh?")

def wordcheck(word,user):
  """Checks inputed words for impossible words
  """
  if len(word) > 45:
    print("Too long to be a word please try again")
    addnewword(user)
  if word.isdigit() == True:
    print('No numbers haha, try again')
    addnewword(user)
  if word == None:
    print("Error please try again")
    addnewword(user)
  if word == "":
    print("Nothing leh try again")
    addnewword(user)
  else:
    pass

def definitioncheck(meaning,username):
  """Checks definition inputted
  """
  if meaning == None:
    print("Error please try again")
    addnewword(username)
  if meaning == "":
    print("Nothing leh try again")
    addnewword(username)

def popquiz(user):
  """Tests user on words they already learnt only effective when there is a large collection of words
  """
  numbercheck = 0
  totalwords = 0
  for person, theirdictionary in everything.items():
    if person == user:
        numbercheck += 1
        for word,meaning in theirdictionary.items():
          totalwords +=1
        testdictionary = theirdictionary
  if numbercheck == 0:
    print("No results found, try again")
    startup()
  print(totalwords)
  rng = list(testdictionary.keys())[randint(0,totalwords-1)]
  string = "do you know the meaning of",rng,"yes/no/stop/skip"
  questionanswer = input(string)
  if questionanswer == "yes":
    print("Yay next")
  if questionanswer == 'no':
    print("Heres the meaning",testdictionary[rng])
  if questionanswer == 'stop':
    goagain()
  if questionanswer == "skip":
    pass
  popquiz(user)

startup()

#startup()