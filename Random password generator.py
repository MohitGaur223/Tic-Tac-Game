import random
text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&.*"

def gen_pass(n,l):
    for i in range(n):
        passoward = ""
        for j in range(l):
            passoward += random.choice(text)
        print(passoward)

n = int(input("enter the number of password you want : " ))
l = int(input("enter the length of the password you want : " ))

gen_pass(n,l)
        
    
