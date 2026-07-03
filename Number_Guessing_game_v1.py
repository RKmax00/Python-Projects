import random

highscore = 99999

level = {
    "easy" : 10,
    "medium" : 50,
    "hard" : 100,
    "hardest" : 1000
    }
while True:
    lvl = input("choose difficulty level (levels- easy/medium/hard/hardest): ").lower().strip()
    if (lvl not in level):
        print("invalid argument") 
    else:               
        number = random.randint(1, level.get(lvl))
        if(level.get(lvl) == 10):
            attempt_limit = 2
        elif(level.get(lvl) == 50):
            attempt_limit = 4    
        elif(level.get(lvl) == 100):
            attempt_limit = 9    
        elif(level.get(lvl) == 1000):
            attempt_limit = 14
        
        attempt = 0     
        while True:
            guess = int(input("guess: "))
            attempt += 1
            if(guess==number):
                print("Congratulations!!")
                print(f"nice bro! it took you {attempt} attempts to guess the correct number")            
                if(highscore>=attempt):
                    highscore = attempt
                    print(f"new highscore is {highscore}!!")
                else:
                    print(f"current highscore is {highscore}")            
                break
            elif(guess>level.get(lvl) or guess<1 ):
                print("invalid guess ")    
            elif(number>guess):
                print("Too low! Try higher number buddy")
            elif(number<guess):
                print("Too high! Try lower number buddy")
            if(attempt == 5):
                if(number%2 == 0):
                    print("Hint - its a even number good luck")
                else:
                    print("Hint - its a odd number good luck")
            if(attempt == 10):
                print(f"The number is in between {number-random.randint(1, 25)} and {number+random.randint(1, 25)}")                
            if(attempt>attempt_limit):
                print("game over!!")
                print(f"gg bro! it took you {attempt} attempts")
                break    
    play_again = input("do you want to play again (y/n): ")
    if(play_again == "n"):
        break
    elif(play_again == "y"):
        print("Good luck")
    else:
        print("invalid argument")
        break
              