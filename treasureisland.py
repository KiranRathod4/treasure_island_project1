# project treasure island
print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`''')

print("wellcome to treasure island")
print("your mission is to find the treasure")

choice1 = input('you have came to a lake ,where do you want to go? type "left" or "right?"\n')
if choice1 == "left":
  choice2 = input('you have came to a lake , there is an island in the middle of the lake , type "wait" to wait for the boat. or type "swim" to swim across\n')
  
  if choice2 == "wait":
    choice3 = input("you have arrived at the island unharmed , there is a house with 3 doors , one red , one yellow and one blue , which colour do you choose?\n")
    if choice3 == "red":
      print("it is a room full of fire , game over")
    elif choice3 == "yellow":
      print("you found the treasure , you win")
    elif choice3 == "blue":
      print("you enter a room of beasts , game over")
    else:
      print("you choose a door that does not exist , game over")
else:
  print("you fall into hole, game over")