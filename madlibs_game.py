#Madlibs game


#Loop to play the game
while True:
    accept_game = input("This is a simple madlibs game, press (y) to continue: ").lower()
    if accept_game == "y":
        break

#Variables assigned to input functions to ask the user for answers which are stored as strings
name = input("Please enter a name:\n")
profession = input("Please write a type of profession:\n")
workplace = input("Please enter a type of workplace:\n")
emotion = input("Please enter an emotion:\n")
clothing = input("Please enter a piece of clothing:\n")
office_supply = input("Please enter an office supply:\n")
past_tense_verb = input("Please enter a past tense verb:\n")
coworkers_name = input("Please enter a coworkers name:\n")
loud_noise = input("Please enter a loud noise:\n")
object = input("Please enter an object: \n")

#Making a madlibs variable assigned to the story and keywords are then inserted through the f string with embedded variables
madlibs = f"This morning, {name}, a dedicated {profession}, walked into the {workplace} feeling {emotion}.\n"\
    f"Everything was going normally until they realised forgotten to wear their {clothing}.\n"\
    f"Trying to play it cool, they grabbed a {office_supply} and pretended it was all part of a new trend.\n"\
    f"Things got worse when they accidentally {past_tense_verb} in front of their boss, {coworkers_name}.\n"\
    f"Suddenly, there was a loud {loud_noise}, and everyone turned to stare.\n"\
    f"It turns out someone had accidentally triggered the building's alarm with a {object}.\n"\
    f"Needless to say, it was a Monday to remember."

#Print madlibs variable
print(madlibs + "\n Thanks for playing, hopefully you found this game fun!")



