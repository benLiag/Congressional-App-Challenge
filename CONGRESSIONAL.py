import time
import random 

def countdown_timer(seconds):
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer_display = '{:02d}:{:02d}'.format(minutes, secs)
        time.sleep(1)
        seconds -= 1

list = ["How many calories do you eat per day?", "On a scale of 1-10, how much do you enjoy grains like rice and bread?", "On a scale of 1-10, how much do you enjoy proteins like beef and chicken?", "On a scale of 1-10, how much do you enjoy fruits and vegetables?", "On a scale of 1-10, how comfortably would you like to live? 1 being homeless, 10 being a mansion", "How much money do you want leftover for personal endeavors like vacations?"]

b = False
while b == False:
    try:
        money = int(input("What's your monthly income in US Dollars? "))
        b = True
        if money <= 0:
            print("Please enter a number greater than 0!")
            b = False
    except:
        print("Please enter a valid number.")
        b = False

for i in range(len(list)):
    works = False
    while works == False:
        try:
            print()
            m = int(input(list[i]+ " "))
            works = True
            if i == 0:
                if m < 1000 or m > 10000:
                    print("Please enter a number between 1000 and 10000!")
                    works = False
            elif i == 5:
                if m < 0 or m > money:
                    print(f"Please enter a number between 0 and {money}!")
                    works = False
            else:
                if m < 1 or m > 10:
                    print("Please enter a number between 1 and 10!")
                    works = False
        except:
            print("Please enter a valid number.")
            works = False
    

print("")

for i in range(random.randint(2,5)):
    countdown_timer(random.randint(1,3))
    print("Calculating...")

input("Results are ready! Press enter to see your suggested budget!")

mon = ["You should spend:", "$0 on grains", "$0 on proteins", "$0 on fruits and vegetables", "$0 on housing", "$0 on utilities", "$0 on personal endeavors", "You need to spend ALL your money on GAMBLING!!!!!!"]
for i in mon:
    print(i)
    countdown_timer(2)

if input("Any questions? y/n ") == "n":
    print("See you later!")
else:
    print("Why should you gamble? \nThe old saying goes that 99% of gamblers quit before they win big, but the number is actually closer to 100%. \nIf you gamble for your entire life, it is almost impossible to NOT win at some point. \nRemember. It's not an addiction - it's dedication.")