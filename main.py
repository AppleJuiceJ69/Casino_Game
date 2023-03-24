import random
import time
#casino slot game
# if person rolls three in a row he wins, or more depending on how much we want to use
# has to have a quit scenario- break statement
# has to have restart-
# gets a set of money at the start of the game
# every win he gets 500, every mega win he gets the jackpot. 
# point system
points = 500
jackPot = 1000
lose = 0


# function that runs each time you spin, and gets points if you win at slots.
def randomCasino():
    rand1 = random.randint(1,10)
    rand2 = random.randint(1,10)
    rand3 = random.randint(1,10)

    if rand1 == rand2 or rand1 == rand3 or rand2 == rand3:
        print('you win 500 points')
        print(points + 500)
        
    else:
        
        print('-100 points')
        print(points - 100)
    if rand1 == rand2 and rand2 == rand3 and rand1 == rand3:
        print('you won the jackpot')
        points + jackPot
        print(points + jackPot)
       
    else: 
        print('not jackpot')
    if points == 0:
        print('Gameover')
    
    print(f' [{rand1}] [{rand2}] [{rand3}]', '\n', '\n', '\n')
    
    
    
randomCasino()

# spins and calls the function each time you type in spin, else it quits
for i in range(10):
   
    spin = int(input('Type 5 to spin again or -type any key to quit- : '))
    if spin == 5:
        randomCasino()
        i+= 1

    else:
        print(f'you quitted at {time.ctime() }')
        break
    
    #if we win the jackpot, then we also have 500 increased points we don't want that.- another problem
    # we also need a lose case scenerio
    # another problem is that the points system don't update every time we recall the function
    
    
    
#readme- we have all of our point systems at the top, and almost all of our code is inside of a function which makes it reusable.
#in the function constits of 3 random things stored inside of variables, when we get a value for each it pops up. As soon as we get three in a row we win.
# Everytime we hit spin it goes runs a conditional that runs the loop again, and then it runs the function, if we want to leave we quit. 
        


        
    


