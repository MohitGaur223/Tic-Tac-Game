import random
x=0
while x==0:
    key= input("enter (y) tok roll again for exit (n)")
    if(key == "y"):
        number = random.randint(1, 6)
        if number == 1:
            print("--------")
            print("[      ]")
            print("[   0  ]")
            print("[      ]")
            print("--------")

        if number == 2:
            print("--------")
            print("[   0   ]")
            print("[       ]")
            print("[   0   ]")
            print("--------")
        if number == 3:
            print("--------")
            print("[   0   ]")
            print("[   0   ]")
            print("[   0   ]")
            print("--------")
        if number == 4:
            print("--------")
            print("[ 0  0 ]")
            print("[      ]")
            print("[ 0  0 ]")
            print("--------")
        if number == 5:
            print("--------")
            print("[ 0  0 ]")
            print("[   0  ]")
            print("[ 0  0 ]")
            print("--------")
        if number == 6:
            print("--------")
            print("[ 0  0 ]")
            print("[ 0  0 ]")
            print("[ 0  0 ]")
            print("--------")
    elif key == "n" :
        exit()
    else:
        print("enter correct option")


