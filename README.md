## Python Word Wall

## Screenshots

![Image of Startup](https://image.ibb.co/eWC9Yz/Screen_Shot_2018_08_08_at_10_28_25_PM.png)

## Tech/framework used

<b>Built with</b>
- [Python3](https://www.python.org/)

## Features
This project offers a easy way to learn and store new words and to test yourself on them

## Code Example

Adding a new word
```python
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
```

## Installation
To run the program simply download files.

Make sure they are in the same directory.

Run the main.py file.

Check that mySavedDict has a blank dictionary. 

![Image of Startup](https://i.imgur.com/OJP2Pbj.gif)


## Tests
No tests currently aivailable 3 marks gone rip.

## How to use?
Basically there are five main functions you can use (new word/delete word/edit/view/pop quiz/help)

new word is the addnewword function which  Allows user to add new words to word wordwall
Enter new word when prompt what would you like to do is given
**Only allowed for existing users**

delete word is the deleteword functon which Allows user to delete word of choice
words keyed in are case sensitive, hence exact word needs to be keyed in when prompted to, function may not work if word is capped 
**Only allowed for existing users**

edit is the edit function which Allows user to edit exisitng word meanings 
Users are allowed to do so by keying in the word and the new meaning
**only allowed for exisiting users**

view is the view function which allows user to view all of existing words and meanings
**only allowed for exisiting users**

pop quiz is the popquiz function which Tests user on words they already learnt only effective when there is a large collection of words **only allowed for existing users**

Example

![Image of Startup](https://i.imgur.com/xBWBBgL.gif)
  

## Credits
Computer elective programme in Raffles Insitution.
Ryan and Luck Heng.


© [Pak Wai](2018)
