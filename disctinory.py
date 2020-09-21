import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def meening(world):
    world = world.lower()
    if world in data:
         return data[step]
    elif world.title() in data:
        return data[world]
    elif world.upper() in data:
        return data[world]
    elif len(get_close_matches(world, data.keys()))>0:
        print(" you may searching for %s " %get_close_matches(world, data.keys())[0])
        deci = input( " enter Y for yes or n for No ").upper()
        if deci=="Y":
             return data[get_close_matches(world, data.keys())[0]]
        elif deci=="N":
            return("You may enter wong keyword : Try again")
        else:
            return ( " yowu enter wrong key enter Y or N")
    else:
        return (" You may enter wong keyword : Try again ")

world = input(" Enter you world : ")
output = meening(world)
print(output)


