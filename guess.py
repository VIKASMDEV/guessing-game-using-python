import random
while True:
    randomnumber=random.randint(1,5)
    
    print("hello there whts ur name ?")
    name=input()
    print("guess the number")
    c=0
    for i in range (5):
        guess=int(input())
        
        c=+i+1
        if guess>randomnumber:
         print("guessed number is very high ")
        elif guess<randomnumber:
         print("guessed number is too low")
        else: 
         break
        
    if guess==randomnumber:
       print(f"perfect {name}!! you have gusse it corect")
       print(f"{name} great job you guessed it in {c} tries")

    print("Do you ant to play again? Y/N")
    answer=input()
    if answer=='y' and answer=='Y':
      continue
    if answer=='n' and answer=='N':
      print("bye thank for playing")
      SystemExit 
 