#Password Generator

import random

def generate_password():
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
                  't','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    user_prompt = int(input("Enter Length Of The Password: "))
    password = ""
    for x in range(user_prompt):
        password += random.choice(characters)
    print("Your Generated Password is:", password)

generate_password()
