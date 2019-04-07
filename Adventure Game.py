import random
import time

output = ("\nSeems like I do have an alcohol problem, mom was right!",
          "\nGod, my head is killin me!",
          "\nSmells like someone took a shit in here...",
          "\nI don't think im gonna make it out alive...",
          "\nWhy must it always be me?",
          "\nAll that Call of Duty training better be worth it right now...")

output2 = ("\nSeems like this fatso's asleep with his hands in a bag of Cheetos, Yuck!",
             "\nWho the hell is this guy, and what is he trying to do with me?",
             "\nI better keep quiet now.. this could turn ugly real quick",
             "\nHe seems like the real deal, I know, he's done this before..",
             "\nI hope he's phone doesn't ring right now!")

inventory = []
light = []
kidnapper = []


def room():
    again = True
    user_pos = "back"
    print("\nYou bit them good. Now your free, and there's a door in front of you.")
    while again:
         print("Which direction would you like to move? (Front / Back / Left / Right)")
         user_input = input().lower()
         if user_input == user_pos:
            print("\nYou can't move in that direction anymore, try again.")
         else:
            if user_input == "front":
               if "axe" in inventory:
                   print("\nGood job! You went shining on that door like a mad man.")
                   print("\nNow there's a stairway heading down and you can hear loud noises from the TV")
                   again = False
                   hall()
               else:
                  print("\nIt's locked! There should be something in the room that you can use to open it.")
                  user_pos = "front"
            elif user_input == "left":
               if "axe" in inventory:
                   print("\nYou already picked up the axe. You should go for the door.")
               elif "axe" not in inventory:
                   while again:
                         print("\nThere's an axe, do you wanna pick it up? [Y/N]")
                         pick_up = input().lower()
                         if pick_up == "y" or pick_up == "yes":
                            print("\nYou have picked up the axe.")
                            inventory.append("axe")
                            break
                         elif pick_up == "help":
                            help()
                         elif user_input == "exit":
                             print("\nYou have left the game, goodbye!")
                             exit()
                         else:
                            print("\nYou didn't pick up the axe.")
                            break
               user_pos = "left"
            elif user_input == "right":
               print(random.choice(output))
               print("There's nothing useful here.")
               user_pos = "right"
            elif user_input == "back":
                print(random.choice(output))
                print("There's nothing useful here.")
                user_pos = "back"
            elif user_input == "help":
                help()
            elif user_input == "exit":
                print("\nYou have left the game, goodbye!")
                exit()
            else:
                print("\nThat's an invalid answer, please try again.")
                again = True

def hall():
    again = True
    user_pos = "back"
    time.sleep(2)
    print("So you creep down the steps... and find yourself in a living room")
    time.sleep(2)
    print("Looks like someones asleep on the couch, they left the TV on.."
          "\nYour anxiety kicks in and you start looking for a way out")
    time.sleep(6)
    print("\nThere's a door to your right and a kitchen to your left")
    time.sleep(1)
    while again:
         print("Which direction would you like to move? (Front / Back / Left / Right)")
         user_input = input().lower()
         if user_input == user_pos:
            print("\nYou can't move in that direction anymore, try again.")
         else:
             if user_input == "right":
                while again:
                      print("\nThe door is locked, do you wanna use the axe? [Y/N]")
                      use_axe = input().lower()
                      if use_axe == "y" or use_axe == "yes":
                         if "dead" not in kidnapper:
                             print("\nBad choice! It's a steel door and you woke up the kidnapper."
                                   "\nHe shot you in the face!")
                             break
                         else:
                             print("You broke free! Always remember to drink responsibly, Cheers mate!")
                             print("The game has ended, thank you for playing Captive.")
                             exit()
                      elif use_axe == "n" or use_axe == "no":
                         print("\nOkay, find another way out.")
                         break
                      elif use_axe == "help":
                           help()
                      elif user_input == "exit":
                          print("\nYou have left the game, goodbye!")
                          exit()
                      else:
                         print("\nThat's an invalid answer, please try again.")
                user_pos = "right"
             elif user_input == "front":
                  if "shotgun" in inventory:
                      print("\nKaboom! You shot him right at his temple, that's some cold blooded murder right there.")
                      print("All those years of COD finally paid off, head for the door now!")
                      kidnapper.append("dead")
                  else:
                      print(random.choice(output2))
                      print("Maybe there's something in the kitchen")
                  user_pos = "front"
             elif user_input == "back":
                 print(random.choice(output))
                 print("There's nothing here.")
                 user_pos = "back"
             elif user_input == "left":
                  if "on" not in light:
                     while again:
                         print("\nThe kitchen is dark, do you wanna turn the lights on? [Y/N]")
                         light_on = input().lower()
                         if light_on == "yes" or light_on == "y":
                            light.append("on")
                            kitchen_light()
                            break
                         elif light_on == "no" or light_on == "n":
                             print(random.choice(output))
                             print("There's nothing here.")
                             break
                         elif light_on == "help":
                              help()
                         elif light_on == "exit":
                             print("\nYou have left the game, goodbye!")
                             exit()
                         else:
                             print("\nThat's an invalid answer, please try again.")
                  else:
                      if "shotgun" in inventory:
                          print(random.choice(output2))
                      else:
                          kitchen_light()
                  user_pos = "left"
             elif user_input == "help":
                  help()
             elif user_input == "exit":
                 print("\nYou have left the game, goodbye!")
                 exit()
             else:
                 print("\nThat's an invalid answer, please try again.")
                 again = True


def kitchen_light():
    again = True
    while again:
        print("\nGood job! Now you see a shotgun on the kitchen counter, do you wanna pick it up? [Y/N]")
        shotgun = input().lower()
        if shotgun == "yes" or shotgun == "y":
           inventory.append("shotgun")
           print("\nYou have picked up the shotgun.")
           print("Your back near the stairs, and the couch is in front of you.")
           break
        elif shotgun == "no" or shotgun == "n":
           print("\nYou did not pick up the shotgun.")
           break
        elif shotgun == "help":
            help()
        elif shotgun == "exit":
            print("\nYou have left the game, goodbye!")
            exit()
        else:
            print("\nThat's an invalid answer, please try again.")


def story_start():
    print("You knocked out after a few round of shots at a party.")
    time.sleep(2)
    print("The next morning, you woke up with your hands tied to a chair in a room.")
    time.sleep(3)
    print("You scream for help but no one can hear you.")
    time.sleep(2)
    print("As you marvel upon the unfamiliar setting, you realise the ropes were lose and you could break free.")
    time.sleep(3)

def first_test():
    print("\nWhat will you do: (Type A or B into the box)")
    time.sleep(2)
    print("a. continue screaming!")
    print("b. or bite through the ropes.")
    user_input = input().lower()
    if user_input == "a":
        print("\nBad choice, you pissed of the kidnapper. He shot you in the face! \nTry again.")
        first_test()
    elif user_input == "b":
        room()
    elif user_input == "help":
        help()
        first_test()
    elif user_input == "exit":
        print("\nYou have left the game, goodbye!")
        exit()
    else:
        print("\nThat is the wrong word, try again.")
        first_test()

def help():
    print("\nHi there "+ name +"! Your currently playing Captive!")
    print("\nIn each room, you will be told which direction you can go.")
    print("You can move FRONT, BACK, LEFT or RIGHT by typing that direction into the box.")
    print("You can also pick up items that you will need in your journey.")
    print("They will present themselves in text, and you will be able to pick them up.")
    print("Type HELP to replay this or EXIT to quit the game.\n")

def play_game():
    help()
    again = True
    while again:
         print("Would you like to start playing? [Y/N]")
         user_input = input().lower()
         if user_input == "y" or user_input == "yes":
            print("\n=================================================================\n")
            story_start()
            first_test()
            again = False
         elif user_input == "n" or user_input == "no" or user_input == "exit":
            print("That's too bad, see ya!")
            exit()
         elif user_input == "help":
            play_game()
            again = True
         else:
            print("\nThat's an invalid answer, please try again.")
            again = True

print("Please enter your name")
name = input().capitalize()
play_game()