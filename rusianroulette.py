''' 
place this file in Desktop folder
go to terminal/powershell and type the following command:
    cd Desktop/;python3 rusianroulette.py
or 
    cd Desktop/ 
    hit enter and type
    python3 rusianroulette.py
'''
''' 
twitter:    https://twitter.com/GilfoyleKhan
github:     https://github.com/GilfoyleKhan

'''
import random
def russianroulette():
    select_number=  1   #change number here
    while True:
        enter=str(input("< :click enter: >"))
        if enter=='' or type(str):
            guess=random.randrange(0,6)
            if guess==select_number:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("\n")
                print(f"!!!!!!!!!!!!!!!!you are doom {guess}!!!!!!!!!!!!!!!!!!")
                print("\n")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                print("thank god",guess)
russianroulette()

