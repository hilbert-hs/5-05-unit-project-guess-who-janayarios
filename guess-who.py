import random



################### Character Dictonary ################### 
# "": {
#     "current status": "",
#     "era": "",
#     "reputation": "",
#     "skill": "",
#     "gender": "",
#   }


characters = {
  "George Washington": {
    "current status": "dead",
    "era": "American Revolution",
    "reputation": "good",
    "skill": "leadership",
    "gender": "male",
  },
  "King George III": {
    "current status": "dead",
    "era": "American Revolution",
    "reputation": "poor",
    "skill": "angering people",
    "gender": "male"
  },
  "Herbert Hoover": {
    "current status": "dead",
    "era": "Gilded Age",
    "reputation": "poor",
    "skill": "destroying the economy",
    "gender": "male",
  },
  "Rosa Parks": {
    "current status": "dead",
    "era": "Civil Rights Movement",
    "reputation": "good",
    "skill": "activism",
    "gender": "female",
  },
  "MLK": {
    "current status": "dead",
    "era": "Civil Rights Movement",
    "reputation": "good",
    "skill": "activism",
    "gender": "male",
  },
  "Genghis Khan": {
    "current status": "dead",
    "era": "ancient history",
    "reputation": "ruthless",
    "skill": "combat",
    "gender": "male",
  },
  "T-rex": {
    "current status": "oil",
    "era": "ancient history",
    "reputation": "ruthless",
    "skill": "combat",
    "gender": "not always the same",
  },
  "Marie Antoinette": {
    "current status": "dead",
    "era": "French Revolution",
    "reputation": "poor",
    "skill": "angering people",
    "gender": "female"
  },
  "King Louis XVI": {
    "current status": "dead",
    "era": "French Revolution",
    "reputation": "poor",
    "skill": "angering people",
    "gender": "male"
  },
} 

##################### Game Functions ###################### 
secretChar = random.choice(list(characters))

def list_char(_dct):
  for person in _dct:
    print(f"\n{person}\nCurrent status: {_dct[person]["current status"]}\nEra: {_dct[person]["era"]}\nReputation: {_dct[person]["reputation"]}\nSkill: {_dct[person]["skill"]}\nGender: {_dct[person]["gender"]}\n")

def ask(_trait, _dct, _secretChar):
  userQuestion = ""
  while userQuestion not in _trait:
    userQuestion = input("What trait would you like to know?: ")
  print(f"The secret character's {userQuestion} is {_dct[_secretChar][userQuestion]}")
  
  


def guess(secretChar):
  userGuess = input("Who do you think was the secret character?: ")
  if userGuess != secretChar:
    print(f"Nope! the secret character was {secretChar}")
  else:
    print("Correct!")

def help(_commands):
  print(f"\nHere are the commands you can do: {_commands}\n")

def quit():
  pass


####################### Game Loop ######################## 

turns = 2
commands = ["list", "ask", "guess", "quit", "help"]
traits = ["current status", "era", "reputation", "skill", "gender"]
userCommand = ""

while turns > 0 and userCommand != "quit":
  userCommand = input("What would you like to do?: ")
  if userCommand not in commands:
    print("That's not an option!")
  else:
    if userCommand == "list":
      list_char(characters)
    if userCommand == "help":
      help(commands)
    if userCommand == "ask":
      ask(traits, characters, secretChar)
      turns -= 1
    if userCommand == "guess":
      turns = 0

if userCommand != "quit":
  guess(secretChar)

