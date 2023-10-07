# IMPORTS
import random as rand
import time 
# IMPORTS

# FUNCTION + CLASS
def question(difficulty, number):
    match difficulty:
        case 1: # TWO VARIABLE (ADD SUB)
            x = rand.randint(0,9)
            y = rand.randint(0,9)
            add_sub = rand.randint(0,1)
            print("Question #" + str(number) + " - Easy")
            print("==================")
            match add_sub:
                case 0:
                    print(str(x) + " + " + str(y))
                    if(input("Answer: ") == str(x + y)):
                        return 1
                    else:
                        return 0
                case 1:
                    print(str(x) + " - " + str(y))
                    if(input("Answer: ") == str(x - y)):
                        return 1
                    else:
                        return 0
        case 2: # TWO VARIABLE (MULTI)
            x = rand.randint(0,9)
            y = rand.randint(0,9)
            add_sub = rand.randint(0,1)
            print("Question #" + str(number) + " - Medium")
            print("==================")
            print(str(x) + " * " + str(y))
            if(input("Answer: ") == str(x * y)):
                return 1
            else:
                return 0
        case 3: # THREE VARIABLE (ADD SUB)
            x = rand.randint(0,9)
            y = rand.randint(0,9)
            z = rand.randint(0,9)
            add_sub = rand.randint(0,3)
            print("Question #" + str(number) + " - Intermediate")
            print("==================")
            match add_sub:
                case 0:
                    print(str(x) + " + " + str(y) + " - " + str(z))
                    if(input("Answer: ").strip() == str(x + y - z)):
                        return 1
                    else:
                        return 0
                case 1:
                    print(str(x) + " - " + str(y) + " + " + str(z))
                    if(input("Answer: ").strip() == str(x - y + z)):
                        return 1
                    else:
                        return 0
                case 3:
                    print(str(x) + " - " + str(y) + " - " + str(z))
                    if(input("Answer: ").strip() == str(x - y - z)):
                        return 1
                    else:
                        return 0
                case 3:
                    print(str(x) + " + " + str(y) + " + " + str(z))
                    if(input("Answer: ").strip() == str(x + y + z)):
                        return 1
                    else:
                        return 0
        case 4: # THREE VARIABLE (ADD SUB MULTI)
            x = rand.randint(0,9)
            y = rand.randint(0,9)
            z = rand.randint(0,9)
            add_sub_mul = rand.randint(0,3)
            print("Question #" + str(number) + " - Difficult")
            print("==================")
            match add_sub_mul:
                case 0:
                    print(str(x) + " + " + str(y) + " * " + str(z))
                    if(input("Answer: ").strip() == str(x + y * z)):
                        return 1
                    else:
                        return 0
                case 1:
                    print(str(x) + " - " + str(y) + " * " + str(z))
                    if(input("Answer: ").strip() == str(x - y * z)):
                        return 1
                    else:
                        return 0
                case 2:
                    print(str(x) + " * " + str(y) + " - " + str(z))
                    if(input("Answer: ").strip() == str(x * y - z)):
                        return 1
                    else:
                        return 0
                case 3:
                    print(str(x) + " * " + str(y) + " + " + str(z))
                    if(input("Answer: ").strip() == str(x * y + z)):
                        return 1
                    else:
                        return 0
        case 5: # THREE SIGNED VARIABLE (ADD SUB MULTI)
            x = rand.randint(-9,9)
            y = rand.randint(-9,9)
            z = rand.randint(-9,9)
            add_sub_mul = rand.randint(0,3)
            print("Question #" + str(number) + " - Hard")
            print("==================")
            match add_sub_mul:
                case 0:
                    print(str(x) + " + " + str(y) + " * " + str(z))
                    if(input("Answer: ").strip() == str(x + y * z)):
                        return 1
                    else:
                        return 0
                case 1:
                    print(str(x) + " - " + str(y) + " * " + str(z))
                    if(input("Answer: ").strip() == str(x - y * z)):
                        return 1
                    else:
                        return 0 
                case 2:
                    print(str(x) + " * " + str(y) + " - " + str(z))
                    if(input("Answer: ").strip() == str(x * y - z)):
                        return 1
                    else:
                        return 0
                case 3:
                    print(str(x) + " * " + str(y) + " + " + str(z))
                    if(input("Answer: ").strip() == str(x * y + z)):
                        return 1
                    else:
                        return 0 

class Scoreboard:
    def __init__(self, scoreboard = {}):
        self.scoreboard = scoreboard
    
    def add_to_scoreboard(self):
        self.scoreboard

class Player:
    def __init__(self, name, best_time = 0, fails = 0):
        self.name = name
        self.best_time = best_time
        self.fails = fails

    def set_best_time(self, new_time):
        self.best_time = new_time

    def add_fail(self):
        self.fails = self.fails + 1
    
    def get_name(self):
        return self.name
# FUNCTION + CLASS
        
# STARTING SCREEN            
print("=========================")
print("Welcome to Speedrun Math!")
print("=========================")

name = input("Please enter your name: ")
player = Player(name)

print("You will be timed for the next 10 math questions.")
print("Do not miss a single question!")
print("Good luck...")
input("\nPress 'Enter'to begin: ")
# STARTING SCREEN

# GAME 
num = 1
while(num < 11):
    start = time.time()
    for i in range(1,6):
        print("")
        if(question(i, num) == 1):
            num = num + 1
            print("Correct!")
            print("==================")
        else:
            print("\nYOU FAILED!")

            break
        print("")
        if(question(i, num) == 1):
            num = num + 1
            print("Correct!")
            print("==================")
        else:
            print("\nYOU FAILED!")
            break
    end = time.time()

    print("\nYou elapsed: " + str(end - start) + " seconds!")
    break

