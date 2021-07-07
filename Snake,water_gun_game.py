import random


# this is the function in it will show who is the winner

def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

    

# in this function the computer will choose an option automatic
print("Comp turn: Snake(s) Water(w) or Gun?(g)")
randcomp = random.randint(1,3)
if randcomp == 1:
    Comp = 's'
elif randcomp == 2:
    Comp = 'w'
elif randcomp == 3:
    Comp = 'g'

# in this function it will take the input from the user

You = input("Your turn: Snake(s)  Water(w) or Gun?(g)")

a = game(Comp,You)

print(f"Comp choose {Comp}")
print(f"you choose {You}")


if a == None:
    print("This is a tie!")
elif a:
    print("You win!")
else:
    print("You loose!")